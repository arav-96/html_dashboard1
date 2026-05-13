# DRG Payment Integrity Dashboard

## Overview
A comprehensive, interactive dashboard for monitoring and analyzing DRG (Diagnosis-Related Group) payment integrity. Built with the Clinical Light color palette for healthcare applications.

## Clinical Light Color Palette
The dashboard implements a professional healthcare color scheme designed for clarity and compliance:

### Background Colors
- **Primary Background**: `#F8FAFC` - Page background
- **Surface**: `#FFFFFF` - Cards, panels, topbar
- **Elevated**: `#F1F5F9` - Table alternate rows, filter tracks

### Accent Colors
- **Navy** `#1D4ED8` - Primary CTA, active tabs, links
- **Teal** `#0D9488` - Findings, positive metrics
- **Red** `#DC2626` - High cost, alerts, no findings
- **Amber** `#D97706` - Outliers, warning flags
- **Violet** `#7C3AED` - MCC condition highlighting

### Text Colors
- **Primary** `#0F172A` - Headings, KPI numbers, table data
- **Secondary** `#64748B` - Labels, headers, subtitles
- **Muted** `#94A3B8` - Placeholders, disabled, no-change

## Features

### 1. KPI Cards
- **Display**: Total Paid Amount, Cases with Findings, Finding Rate, High-Cost Cases
- **Styling**: Navy top border, value in primary text, trend indicators with color coding
- **Trends**: Teal for positive, Red for negative, Muted for neutral

### 2. Filter Panel
- Date Range selection
- Provider filtering
- Condition Type filtering
- Active filter badges showing current selections

### 3. Multi-Tab Interface
- **Overview**: Summary charts and drill-down table
- **Findings**: Cases with findings analysis
- **Condition Analysis**: MCC/CC/Other condition type breakdown
- **Outliers**: High-cost case identification

### 4. Data Visualization
All charts use the standard Chart.js color sequence:
- `#1D4ED8` Navy
- `#0D9488` Teal
- `#D97706` Amber
- `#DC2626` Red
- `#7C3AED` Violet
- `#0EA5E9` Cyan
- `#059669` Green

### 5. Interactive Tables
- **Expandable Rows**: Click case IDs to view detailed findings
- **Color Coding**: 
  - High-cost amounts (>$20K) in red
  - MCC tags with purple background
  - CC tags with blue background
  - Findings with appropriate colored badges
- **Hover Effects**: Rows highlight in light blue (#EFF6FF) on hover
- **Conditional Styling**: Expanded rows show navy left border with context background

### 6. Export & Print
- **CSV Export**: Downloads table data as CSV file
- **Print Stylesheet**: Optimized for printing with proper styling and hidden interactive elements

## File Structure
```
html_page3/
├── index.html          # Main dashboard markup
├── styles.css          # Complete styling with color palette
├── script.js           # Interactive functionality and charts
├── README.md           # This file
├── LAUNCH.bat          # Quick launch script for Windows
└── [image files]       # Reference logos and screenshots
```

## Usage

### Quick Start
1. **Windows Users**: Double-click `LAUNCH.bat` to open the dashboard in your default browser
2. **Manual**: Open `index.html` in any modern web browser

### Interacting with the Dashboard
- **Switch Tabs**: Click tab buttons to view different analysis sections
- **Expand Cases**: Click the expand arrow (▶) in case rows to see detailed findings
- **Filter Data**: Use dropdown selectors to filter by date, provider, or condition type
- **Export**: Click "Export CSV" to download table data
- **Print**: Click "Print" to generate a print-friendly version

## Design Rules Applied

### KPI Cards
- Background: White surface with 0.5px border
- Top border: 2px navy accent
- Value font: 20px, 500 weight
- Label font: 11px, secondary text color

### Tables
- Header rows: Elevated background
- Data rows: Alternating surface/elevated backgrounds
- Hover state: Light blue (#EFF6FF)
- Expanded rows: Navy left border with primary background

### Condition Type Tags
- **MCC**: Purple background (#EDE9FE) with dark purple text (#5B21B6)
- **CC**: Blue background (#DBEAFE) with dark blue text (#1E40AF)
- **OTHER**: Elevated background with secondary text

### Conditional Cell Colors
- Amount > $20,000: Red text
- Finding found (exl_finding = 1): Green background (#F0FDF4)
- No finding (exl_nofinding = 1): Red background (#FEF2F2)

### Chart Styling
- Gridlines: Border color at 50% opacity
- Axis labels: Secondary text color
- Tooltips: White background with 0.5px border, primary text color
- Series colors: Exact Chart.js color sequence

### Responsive Design
- Adapts to mobile and tablet screens
- Stacked layout for smaller viewports
- Touch-friendly filter controls

### Print Stylesheet
- All backgrounds: White
- All text: Primary color (#0F172A)
- Borders: Border color (#E2E8F0)
- Hidden elements: Filters, export buttons
- Visible elements: KPIs, charts, pivot table stacked vertically

## Browser Compatibility
- Chrome/Edge: Fully supported
- Firefox: Fully supported
- Safari: Fully supported
- IE 11: Not supported (uses modern CSS Grid and Flexbox)

## Dependencies
- Chart.js 4.4.0 (CDN)
- Chart.js Data Labels Plugin 2.2.0 (CDN)
- No backend required - all data is static sample data

## Customization

### Changing Colors
Edit the CSS variables in `styles.css` `:root` section to modify the entire color scheme:

```css
:root {
    --bg-primary: #F8FAFC;
    --accent-navy: #1D4ED8;
    /* ... etc ... */
}
```

### Adding New Data
Update the table rows and chart data in `index.html` and modify corresponding arrays in `script.js`.

### Modifying Charts
Edit the chart configuration objects in `script.js` for each chart type:
- `createFindingRateChart()`
- `createCostDistributionChart()`
- etc.

## Healthcare Compliance Notes
- All color combinations meet WCAG AA accessibility standards
- No pure black (#000000) or pure white (#FFFFFF) used at page level
- Color palette remains within #F8FAFC to #0F172A range
- Print-friendly design maintains readability without color dependency

## Support
For issues or feature requests, review the code structure:
- HTML: Component markup and data structure
- CSS: Styling, layout, and responsive design
- JavaScript: Interactivity, charts, and data processing

## License
Internal use only for DRG Payment Integrity analysis.

---
**Created**: May 2026
**Version**: 1.0
**Color Palette**: Clinical Light
