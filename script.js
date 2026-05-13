/* ============================================================
   DRG Payment Integrity Dashboard - JavaScript
   ============================================================ */

// ============================================================
// SIDEBAR TOGGLE
// ============================================================

let sidebarOpen = false;

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebarOpen = !sidebarOpen;
    
    if (sidebarOpen) {
        sidebar.classList.add('open');
    } else {
        sidebar.classList.remove('open');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    }
});

// ============================================================
// MENU ITEM SELECTION
// ============================================================

function selectMenuItem(element, menuId) {
    // Remove active class from all menu items
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.classList.remove('active');
    });

    // Add active class to selected item
    element.classList.add('active');

    // Show the correct content pane
    const contentPanes = document.querySelectorAll('.content-pane');
    contentPanes.forEach(pane => {
        pane.classList.remove('active');
    });

    const selectedPane = document.getElementById(menuId);
    if (selectedPane) {
        selectedPane.classList.add('active');
    }
}

// ============================================================
// ROW EXPANSION/COLLAPSE (for future use)
// ============================================================
// ============================================================

function toggleRow(button) {
    const row = button.closest('tr');
    const expandedRow = row.nextElementSibling;

    if (expandedRow && expandedRow.classList.contains('expanded-content')) {
        const isExpanded = expandedRow.style.display !== 'none';
        
        if (isExpanded) {
            expandedRow.style.display = 'none';
            button.classList.remove('expanded');
        } else {
            expandedRow.style.display = 'table-row';
            button.classList.add('expanded');
        }
    }
}

// ============================================================
// COLLAPSIBLE IMAGE PANELS
// ============================================================

function togglePanel(button) {
    const card = button.closest('.category-card');
    const collapseBody = card.querySelector('.collapse-body');
    if (!collapseBody) return;

    const isOpen = collapseBody.classList.toggle('open');
    if (card.querySelector('.category-badge').textContent === 'D') {
        button.textContent = isOpen ? 'Hide details' : 'Show details';
    } else {
        button.textContent = isOpen ? 'Hide details' : 'Show pre/post details';
    }
}
