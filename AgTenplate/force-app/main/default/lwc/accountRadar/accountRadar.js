import { LightningElement, api, track, wire } from 'lwc';
import { getRecord } from 'lightning/uiRecordApi';
import { NavigationMixin } from 'lightning/navigation';
import { ShowToastEvent } from 'lightning/platformShowToastEvent';
import getNearbyAccounts from '@salesforce/apex/AccountRadarController.getNearbyAccounts';

const ACCOUNT_FIELDS = [
    'Account.Id',
    'Account.Name',
    'Account.BillingLatitude',
    'Account.BillingLongitude'
];

export default class AccountRadar extends NavigationMixin(LightningElement) {
    @api recordId;
    @api proximityRadius = 10; // Default radius in kilometers
    
    @track nearbyAccounts = [];
    @track isLoading = false;
    @track error = null;
    @track currentPage = 1;
    @track itemsPerPage = 5;
    
    currentAccount;
    
    @wire(getRecord, { recordId: '$recordId', fields: ACCOUNT_FIELDS })
    wiredAccount({ error, data }) {
        if (data) {
            this.currentAccount = data;
            this.loadNearbyAccounts();
        } else if (error) {
            this.error = 'Error loading current account: ' + this.getErrorMessage(error);
        }
    }
    
    get showRadar() {
        return !this.isLoading && !this.error && this.nearbyAccounts.length > 0;
    }
    
    get sliderValue() {
        // Cap the slider display value at 20, even if proximityRadius is higher
        return Math.min(this.proximityRadius, 20);
    }
    
    get isCustomRadius() {
        // Check if the radius is set higher than slider max through property
        return this.proximityRadius > 20;
    }
    
    get paginatedAccounts() {
        if (!this.nearbyAccounts || this.nearbyAccounts.length === 0) {
            return [];
        }
        
        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        return this.nearbyAccounts.slice(startIndex, endIndex);
    }
    
    get totalPages() {
        if (!this.nearbyAccounts || this.nearbyAccounts.length === 0) {
            return 0;
        }
        return Math.ceil(this.nearbyAccounts.length / this.itemsPerPage);
    }
    
    get hasNextPage() {
        return this.currentPage < this.totalPages;
    }
    
    get hasPreviousPage() {
        return this.currentPage > 1;
    }
    
    get pageInfo() {
        if (!this.nearbyAccounts || this.nearbyAccounts.length === 0) {
            return '';
        }
        const startItem = (this.currentPage - 1) * this.itemsPerPage + 1;
        const endItem = Math.min(this.currentPage * this.itemsPerPage, this.nearbyAccounts.length);
        return `Showing ${startItem}-${endItem} of ${this.nearbyAccounts.length} accounts`;
    }
    
    get showPagination() {
        return this.nearbyAccounts && this.nearbyAccounts.length > this.itemsPerPage;
    }
    
    get pageNumbers() {
        if (this.totalPages <= 1) return [];
        
        const pages = [];
        const maxVisiblePages = 5;
        let startPage = Math.max(1, this.currentPage - Math.floor(maxVisiblePages / 2));
        let endPage = Math.min(this.totalPages, startPage + maxVisiblePages - 1);
        
        if (endPage - startPage + 1 < maxVisiblePages) {
            startPage = Math.max(1, endPage - maxVisiblePages + 1);
        }
        
        for (let i = startPage; i <= endPage; i++) {
            pages.push(i);
        }
        return pages;
    }
    
    get isPreviousDisabled() {
        return !this.hasPreviousPage;
    }
    
    get isNextDisabled() {
        return !this.hasNextPage;
    }
    
    get itemsPerPage5() {
        return this.itemsPerPage === 5;
    }
    
    get itemsPerPage10() {
        return this.itemsPerPage === 10;
    }
    
    get itemsPerPage20() {
        return this.itemsPerPage === 20;
    }
    
    get itemsPerPage50() {
        return this.itemsPerPage === 50;
    }
    
    get pageNumClass() {
        return (pageNum) => {
            const baseClass = 'page-number-btn';
            return pageNum === this.currentPage ? `${baseClass} active` : baseClass;
        };
    }
    
    handleRadiusChange(event) {
        this.proximityRadius = parseInt(event.target.value, 10);
        this.loadNearbyAccounts();
    }
    
    handleItemsPerPageChange(event) {
        this.itemsPerPage = parseInt(event.target.value, 10);
        this.currentPage = 1; // Reset to first page when changing items per page
    }
    
    handleNextPage() {
        if (this.hasNextPage) {
            this.currentPage++;
        }
    }
    
    handlePreviousPage() {
        if (this.hasPreviousPage) {
            this.currentPage--;
        }
    }
    
    handlePageChange(event) {
        const pageNumber = parseInt(event.target.dataset.page, 10);
        if (pageNumber && pageNumber !== this.currentPage) {
            this.currentPage = pageNumber;
        }
    }
    
    loadNearbyAccounts() {
        if (!this.currentAccount || 
            !this.currentAccount.fields.BillingLatitude.value || 
            !this.currentAccount.fields.BillingLongitude.value) {
            this.error = 'Current account must have billing latitude and longitude';
            return;
        }
        
        this.isLoading = true;
        this.error = null;
        
        getNearbyAccounts({
            currentAccountId: this.recordId,
            latitude: this.currentAccount.fields.BillingLatitude.value,
            longitude: this.currentAccount.fields.BillingLongitude.value,
            radiusKm: this.proximityRadius
        })
        .then(result => {
            this.nearbyAccounts = this.processAccountsForRadar(result);
            this.isLoading = false;
        })
        .catch(error => {
            this.error = 'Error loading nearby accounts: ' + this.getErrorMessage(error);
            this.isLoading = false;
        });
    }
    
    processAccountsForRadar(accounts) {
        if (!accounts || accounts.length === 0) {
            return [];
        }
        
        // Filter out accounts with invalid distances
        const validAccounts = accounts.filter(acc => {
            const distance = typeof acc.distance === 'number' ? acc.distance : parseFloat(acc.distance);
            return !isNaN(distance) && distance >= 0;
        });
        
        if (validAccounts.length === 0) {
            return [];
        }
        
        const centerX = 200;
        const centerY = 200;
        const maxRadius = 150; // Maximum radar radius in pixels
        
        return validAccounts.map(account => {
            // Ensure distance is a number
            const distance = typeof account.distance === 'number' ? account.distance : parseFloat(account.distance) || 0;
            
            // Calculate position on radar based on actual distance zones
            const angle = Math.random() * 2 * Math.PI; // Random angle for distribution
            
            // Map distance to radar radius based on search radius and radar zones
            let radius;
            const searchRadius = this.proximityRadius || 10; // Default to 10km if not set
            
            // Calculate what percentage of the search radius this distance represents
            const distancePercentage = Math.min(distance / searchRadius, 1);
            
            // Map to radar zones: 0-50px (green), 50-100px (yellow), 100-150px (red)
            if (distancePercentage <= 0.33) {
                // Green zone: 0-50px radius (0-33% of search radius)
                radius = (distancePercentage / 0.33) * 50;
            } else if (distancePercentage <= 0.67) {
                // Yellow zone: 50-100px radius (33-67% of search radius)
                radius = 50 + ((distancePercentage - 0.33) / 0.34) * 50;
            } else {
                // Red zone: 100-150px radius (67-100% of search radius)
                radius = 100 + ((distancePercentage - 0.67) / 0.33) * 50;
            }
            
            const x = centerX + radius * Math.cos(angle);
            const y = centerY + radius * Math.sin(angle);
            
            // Determine color based on distance percentage of search radius
            let color;
            
            if (distancePercentage <= 0.33) {
                color = '#38a169'; // Green for nearby (0-33% of search radius)
            } else if (distancePercentage <= 0.67) {
                color = '#d69e2e'; // Yellow for medium (33-67% of search radius)
            } else {
                color = '#e53e3e'; // Red for far (67-100% of search radius)
            }
            
            return {
                ...account,
                x: Math.round(x),
                y: Math.round(y),
                color: color,
                colorStyle: `background-color: ${color}`,
                distance: distance, // Store the converted number
                distanceText: `${distance.toFixed(1)} km`
            };
        });
    }
    
    handleAccountClick(event) {
        const accountId = event.target.dataset.accountId;
        if (accountId) {
            this[NavigationMixin.Navigate]({
                type: 'standard__recordPage',
                attributes: {
                    recordId: accountId,
                    objectApiName: 'Account',
                    actionName: 'view'
                }
            });
        }
    }
    
    connectedCallback() {
        // Component lifecycle hook
    }
    
    renderedCallback() {
        // Add hover effects to account dots
        const accountDots = this.template.querySelectorAll('.account-dot');
        accountDots.forEach(dot => {
            dot.addEventListener('mouseenter', this.handleDotHover.bind(this));
            dot.addEventListener('mouseleave', this.handleDotLeave.bind(this));
        });
    }
    
    handleDotHover(event) {
        event.target.setAttribute('r', '8');
        event.target.style.cursor = 'pointer';
    }
    
    handleDotLeave(event) {
        event.target.setAttribute('r', '6');
    }
    
    getErrorMessage(error) {
        // Handle different error formats safely
        if (error && error.body && error.body.message) {
            return error.body.message;
        } else if (error && error.message) {
            return error.message;
        } else if (typeof error === 'string') {
            return error;
        } else {
            return 'An unexpected error occurred';
        }
    }
}