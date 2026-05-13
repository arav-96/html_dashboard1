# DRG Payment Integrity Dashboard - Design System Reference

## Quick Reference: Clinical Light Color Palette

### Color Swatches

```
BACKGROUNDS
■ Primary    #F8FAFC    (Light Sky Blue)
■ Surface    #FFFFFF    (Pure White)
■ Elevated   #F1F5F9    (Very Light Gray Blue)

BORDERS
■ Default    #E2E8F0    (Light Gray Blue)
■ Focus      #BFDBFE    (Cornflower Blue)

ACCENTS
■ Navy       #1D4ED8    (Strong Blue)
■ Teal       #0D9488    (Teal Green)
■ Red        #DC2626    (Bright Red)
■ Amber      #D97706    (Orange)
■ Violet     #7C3AED    (Purple)
■ Cyan       #0EA5E9    (Light Blue)
■ Green      #059669    (Dark Green)

TEXT
■ Primary    #0F172A    (Very Dark Blue)
■ Secondary  #64748B    (Slate Gray)
■ Muted      #94A3B8    (Light Gray)
```

## Component Styling Guide

### 1. KPI Cards

**Structure:**
```html
<div class="kpi-card">
    <div class="kpi-value">$2.4M</div>
    <div class="kpi-label">Total Paid Amount</div>
    <div class="kpi-trend positive">▲ 12.5%</div>
</div>
```

**CSS Properties:**
- Background: White (#FFFFFF)
- Border: 0.5px solid #E2E8F0 (all sides)
- Top Border: 2px solid #1D4ED8 (navy)
- Value Font: 20px, weight 500, color #0F172A (text-primary)
- Label Font: 11px, color #64748B (text-secondary)
- Padding: 20px

**Trend Indicators:**
- Positive (▲): Color #0D9488 (teal)
- Negative (▼): Color #DC2626 (red)
- Neutral (→): Color #94A3B8 (muted)

---

### 2. Data Tables

**Header Row:**
- Background: #F1F5F9 (elevated)
- Font: 12px, uppercase, weight 600, color #64748B (secondary)
- Border: 0.5px solid #E2E8F0
- Padding: 12px 16px

**Data Rows - Alternating Pattern:**
- Odd rows: #FFFFFF (surface)
- Even rows: #F1F5F9 (elevated)
- Font: 13px, color #0F172A (primary)
- Border: 0.5px solid #E2E8F0
- Padding: 12px 16px

**Hover State:**
- Background: #EFF6FF (light blue)

**Expanded Row (Child Content):**
- Background: #F8FAFC (primary background)
- Left border: 2px solid #1D4ED8 (navy)
- Padding: 16px 16px 16px 20px
- Font: 12px, color #64748B (secondary)
- Contains: Details, adjustments, notes

**High-Cost Cells (Amount > $20,000):**
- Text color: #DC2626 (red)
- Font weight: 500

---

### 3. Condition Type Tags

**MCC (Multiple Comorbidities):**
- Background: #EDE9FE (light purple)
- Text: #5B21B6 (dark purple)
- Font: 11px, uppercase, weight 600

**CC (Comorbidity/Complication):**
- Background: #DBEAFE (light blue)
- Text: #1E40AF (dark blue)
- Font: 11px, uppercase, weight 600

**OTHER:**
- Background: #F1F5F9 (elevated)
- Text: #64748B (secondary)
- Font: 11px, uppercase, weight 600

---

### 4. Finding Badges

**Yes - Finding Found:**
- Background: #F0FDF4 (light green)
- Text: #15803D (dark green)
- Font: 11px, weight 600

**No - No Finding:**
- Background: #FEF2F2 (light red)
- Text: #DC2626 (red)
- Font: 11px, weight 600

---

### 5. Filter Dropdowns

**Inactive State:**
- Background: #FFFFFF (surface)
- Border: 0.5px solid #E2E8F0
- Font: 14px, color #0F172A (primary)
- Padding: 8px 12px
- Min-width: 180px

**Hover State:**
- Border color: #1D4ED8 (navy)

**Focus State:**
- Border color: #BFDBFE (focus)
- Box-shadow: 0 0 0 3px rgba(191, 219, 254, 0.3)
- Outline: none

**Active Filter Badge:**
- Background: #EFF6FF (light blue)
- Text: #1D4ED8 (navy)
- Border: 0.5px solid #BFDBFE (focus)
- Font: 12px, weight 500

---

### 6. Tabs

**Tab Header:**
- Background: #FFFFFF (surface)
- Border-bottom: 0.5px solid #E2E8F0
- Padding: 12px 0

**Inactive Tab:**
- Text color: #64748B (secondary)
- No underline

**Active Tab:**
- Text color: #0F172A (primary)
- Underline: 2px solid #1D4ED8 (navy)
- Position: bottom border

---

### 7. Chart Styling

**Color Sequence (for series):**
1. #1D4ED8 (Navy)
2. #0D9488 (Teal)
3. #D97706 (Amber)
4. #DC2626 (Red)
5. #7C3AED (Violet)
6. #0EA5E9 (Cyan)
7. #059669 (Green)

**Gridlines:**
- Color: #E2E8F0 (border)
- Opacity: 50%

**Axis Labels:**
- Font size: 11px
- Color: #64748B (secondary)
- Font weight: 500

**Tooltip:**
- Background: #FFFFFF (surface)
- Border: 0.5px solid #E2E8F0
- Text color: #0F172A (primary)
- Padding: 12px
- Border-radius: 4px

---

### 8. Export Buttons

**Default State:**
- Background: #FFFFFF (surface)
- Border: 0.5px solid #E2E8F0
- Font: 13px, weight 500, color #64748B (secondary)
- Padding: 8px 16px
- Border-radius: 4px

**Hover State:**
- Background: #F1F5F9 (elevated)

**Active State:**
- Background: #E8EEF5

---

## Accessibility Standards

✓ All color combinations meet WCAG AA contrast ratio (4.5:1 minimum)
✓ No reliance on color alone to convey information
✓ Sufficient distinction between interactive and non-interactive elements
✓ Color palette works for colorblind users (deuteranopia, protanopia, tritanopia)

### Print Considerations
- All backgrounds convert to white
- All text converts to primary color (#0F172A)
- Borders remain #E2E8F0
- Interactive elements hidden
- Content stacks vertically

---

## Customization Guide

### Modify Global Colors

Edit `styles.css` in the `:root` selector:

```css
:root {
    --bg-primary: #F8FAFC;      /* Change page background */
    --bg-surface: #FFFFFF;      /* Change card background */
    --accent-navy: #1D4ED8;     /* Change primary accent */
    /* ... etc ... */
}
```

All components automatically inherit the new colors.

### Change Table Alternating Rows

In `styles.css`, modify:

```css
.data-table tbody tr:nth-child(odd) td {
    background-color: var(--bg-surface);
}

.data-table tbody tr:nth-child(even) td {
    background-color: var(--bg-elevated);
}
```

### Adjust KPI Card Borders

In `styles.css`, modify `.kpi-card`:

```css
.kpi-card {
    border: 0.5px solid var(--border);
    border-top: 2px solid var(--accent-navy);
    /* Adjust these values for different styles */
}
```

### Change Chart Colors

In `script.js`, modify the `chartColors` array:

```javascript
const chartColors = [
    '#1D4ED8',  // Change primary color
    '#0D9488',  // Change secondary color
    /* ... etc ... */
];
```

---

## Best Practices

1. **Consistency**: Always use CSS variables instead of hardcoding hex colors
2. **Accessibility**: Test color combinations for sufficient contrast
3. **Print**: Test print styling regularly
4. **Responsive**: Verify layout on mobile, tablet, and desktop
5. **Focus**: Ensure all interactive elements have visible focus states
6. **Hover**: Provide visual feedback on hover for clickable elements
7. **Disabled**: Use `--text-muted` for disabled states

---

## Common Use Cases

### Highlight a Finding
Apply `.finding-badge.positive` class or set background to #F0FDF4 with text #15803D

### Alert for High Cost
Apply `.high-cost` class or set text color to #DC2626

### Mark as Critical
Apply `.severity-badge.red` class or use background #FEE2E2 with text #7F1D1D

### Indicate Warning
Apply `.severity-badge.amber` class or use background #FEF3C7 with text #92400E

### Show Status
- Active: #0D9488 (teal)
- Inactive: #64748B (secondary)
- Error: #DC2626 (red)

---

## Color Psychology in Healthcare

- **Blue (#1D4ED8)**: Trust, stability, professionalism
- **Teal (#0D9488)**: Healing, positive outcomes
- **Red (#DC2626)**: Urgent alerts, critical findings
- **Green (#059669)**: Healthy, positive metrics
- **Amber (#D97706)**: Caution, requires attention
- **Violet (#7C3AED)**: Special categorization, distinction

---

## Support Resources

- Chart.js Documentation: https://www.chartjs.org/docs/latest/
- WCAG Accessibility: https://www.w3.org/WAI/WCAG21/quickref/
- CSS Variables: https://developer.mozilla.org/en-US/docs/Web/CSS/--*
- Color Contrast Checker: https://webaim.org/resources/contrastchecker/

---

**Last Updated**: May 2026
**Version**: 1.0
**Format**: Text Reference Guide
