// Initialize table sorting for all sortable tables
function initTableSort() {
    const tables = document.querySelectorAll('.sortable-table');
    tables.forEach(table => {
        new Tablesort(table);
    });
}

// Run when page is ready
document.addEventListener('DOMContentLoaded', initTableSort, false);
