from fpdf import FPDF
import datetime

class ConstructionGuidePDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Arial', 'B', 10)
            self.set_text_color(0, 51, 102)
            self.cell(0, 10, 'COMPREHENSIVE BUILDING & CONSTRUCTION GUIDE', 0, 0, 'C')
            self.ln(15)
            self.set_draw_color(0, 51, 102)
            self.line(10, 20, 200, 20)
            self.ln(10)
    
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, f'Page {self.page_no()} | Professional Reference Guide | Transition from LASBCA to Private Development', 0, 0, 'C')
    
    def chapter_title(self, title, color_r, color_g, color_b):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(color_r, color_g, color_b)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_draw_color(color_r, color_g, color_b)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(10)
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 51, 102)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(4)
    
    def body_text(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(4)
    
    def bullet_point(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(0, 0, 0)
        self.cell(5, 6, '•', 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(2)
    
    def draw_box_diagram(self, title, items, x_start=20, y_start=None):
        if y_start is None:
            y_start = self.get_y()
        
        box_width = 170
        box_height = 10
        title_height = 8
        
        self.set_fill_color(230, 240, 255)
        self.set_draw_color(0, 51, 102)
        self.set_font('Arial', 'B', 9)
        
        # Title box
        self.rect(x_start, y_start, box_width, title_height, 'DF')
        self.set_xy(x_start, y_start + 1)
        self.cell(box_width, 5, title, 0, 0, 'C')
        
        y = y_start + title_height
        self.set_font('Arial', '', 8)
        
        for item in items:
            self.set_fill_color(255, 255, 255)
            self.rect(x_start, y, box_width, box_height, 'D')
            self.set_xy(x_start + 5, y + 2)
            self.cell(box_width - 10, 5, item, 0, 0, 'L')
            y += box_height
        
        self.set_y(y + 5)

# Create PDF
pdf = ConstructionGuidePDF()
pdf.set_auto_page_break(auto=True, margin=20)

# Cover Page
pdf.add_page()
pdf.set_fill_color(0, 51, 102)
pdf.rect(0, 0, 210, 297, 'F')
pdf.set_y(100)
pdf.set_font('Arial', 'B', 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 15, 'BUILDING & CONSTRUCTION', 0, 1, 'C')
pdf.cell(0, 15, 'COMPREHENSIVE GUIDE', 0, 1, 'C')
pdf.set_font('Arial', 'B', 14)
pdf.set_text_color(200, 220, 255)
pdf.cell(0, 10, 'Architecture • Civil • Structural • Electrical', 0, 1, 'C')
pdf.cell(0, 10, 'Mechanical • Building Construction', 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Arial', 'I', 12)
pdf.set_text_color(180, 200, 240)
pdf.cell(0, 8, 'Professional Reference for Private Development', 0, 1, 'C')
pdf.cell(0, 8, 'From LASBCA to Private Practice', 0, 1, 'C')
pdf.ln(30)
pdf.set_font('Arial', '', 10)
pdf.set_text_color(150, 170, 200)
pdf.cell(0, 6, f'Date: {datetime.datetime.now().strftime("%B %Y")}', 0, 1, 'C')

# Table of Contents
pdf.add_page()
pdf.chapter_title('TABLE OF CONTENTS', 0, 51, 102)
pdf.set_font('Arial', '', 10)
toc_items = [
    "1. ARCHITECTURAL DESIGN FUNDAMENTALS",
    "2. CIVIL ENGINEERING - SITE & FOUNDATION",
    "3. STRUCTURAL ENGINEERING SYSTEMS",
    "4. ELECTRICAL SYSTEMS & INSTALLATIONS",
    "5. MECHANICAL SYSTEMS (HVAC & PLUMBING)",
    "6. BUILDING CONSTRUCTION METHODS",
    "7. CONSTRUCTION MANAGEMENT & QUALITY CONTROL",
    "8. BUILDING CODES & REGULATIONS",
    "9. MATERIALS & SPECIFICATIONS",
    "10. SUSTAINABLE & SMART BUILDING PRACTICES"
]
for item in toc_items:
    pdf.cell(0, 8, item, 0, 1)
    pdf.ln(2)

# Section 1: Architecture
pdf.add_page()
pdf.chapter_title('1. ARCHITECTURAL DESIGN FUNDAMENTALS', 0, 102, 204)

pdf.section_title('1.1 Building Typologies')
pdf.body_text('Understanding different building types is crucial for proper design and regulation compliance:')
pdf.bullet_point('Residential: Single-family, multi-family, apartment blocks, duplexes')
pdf.bullet_point('Commercial: Office buildings, retail spaces, mixed-use developments')
pdf.bullet_point('Industrial: Warehouses, manufacturing facilities')
pdf.bullet_point('Institutional: Schools, hospitals, government buildings')

pdf.section_title('1.2 Design Process Flowchart')
pdf.draw_box_diagram('ARCHITECTURAL DESIGN PROCESS', [
    '1. CLIENT BRIEF & REQUIREMENTS ANALYSIS',
    '2. SITE ANALYSIS & FEASIBILITY STUDY',
    '3. CONCEPTUAL DESIGN (Schematic Design)',
    '4. DESIGN DEVELOPMENT (Detailed Design)',
    '5. STATUTORY APPROVALS & PERMITS',
    '6. CONSTRUCTION DOCUMENTS',
    '7. TENDER & PROCUREMENT',
    '8. CONSTRUCTION ADMINISTRATION',
    '9. PROJECT HANDOVER & POST-OCCUPANCY'
])

pdf.section_title('1.3 Space Planning Essentials')
pdf.body_text('Key considerations for effective space planning:')
pdf.bullet_point('Minimum room dimensions per building code requirements')
pdf.bullet_point('Circulation spaces: corridors (min 1.2m), stairs, ramps')
pdf.bullet_point('Service areas: kitchens, bathrooms, utility rooms')
pdf.bullet_point('Natural lighting and ventilation requirements')
pdf.bullet_point('Accessibility standards (ramps, elevators, door widths)')

# Section 2: Civil Engineering
pdf.add_page()
pdf.chapter_title('2. CIVIL ENGINEERING - SITE & FOUNDATION', 0, 153, 76)

pdf.section_title('2.1 Site Investigation Process')
pdf.body_text('Before any construction begins, comprehensive site investigation is mandatory:')
pdf.bullet_point('Soil testing: Boring, sampling, laboratory analysis')
pdf.bullet_point('Topographical survey and contour mapping')
pdf.bullet_point('Water table assessment and drainage patterns')
pdf.bullet_point('Geological hazards: erosion, subsidence, seismic activity')

pdf.section_title('2.2 Foundation Types Diagram')
pdf.draw_box_diagram('FOUNDATION SELECTION CRITERIA', [
    'SHALLOW FOUNDATIONS: Strip footing, Pad footing, Raft foundation',
    'DEEP FOUNDATIONS: Pile foundation (driven/cast-in-place), Caisson',
    'SELECTION FACTORS: Soil bearing capacity, Load requirements',
    'WATER TABLE: High water table may require special foundation',
    'ADJACENT STRUCTURES: Impact on neighboring buildings',
    'ECONOMIC CONSIDERATIONS: Cost vs. performance'
])

pdf.section_title('2.3 Site Preparation')
pdf.body_text('Essential site preparation activities:')
pdf.bullet_point('Clearing and grubbing (removal of vegetation)')
pdf.bullet_point('Earthworks: Cut and fill operations')
pdf.bullet_point('Temporary drainage and dewatering')
pdf.bullet_point('Site access and temporary roads')
pdf.bullet_point('Utility connections and temporary services')

# Section 3: Structural Engineering
pdf.add_page()
pdf.chapter_title('3. STRUCTURAL ENGINEERING SYSTEMS', 204, 102, 0)

pdf.section_title('3.1 Structural Systems Comparison')
pdf.draw_box_diagram('STRUCTURAL SYSTEM TYPES', [
    '1. FRAME STRUCTURE: Columns + Beams (RCC/Steel)',
    '2. LOAD BEARING WALL: Walls carry all loads',
    '3. SHEAR WALL SYSTEM: Walls resist lateral loads',
    '4. CORE STRUCTURE: Central core + perimeter columns',
    '5. FLAT SLAB: Direct slab-column connection',
    '6. SPACE FRAME: 3D truss system for large spans'
])

pdf.section_title('3.2 Reinforced Concrete Design')
pdf.body_text('Key elements of RC design:')
pdf.bullet_point('Concrete grades: C20/25, C25/30, C30/37, C40/50 (strength in MPa)')
pdf.bullet_point('Reinforcement steel: High yield (460 N/mm²), Mild steel (250 N/mm²)')
pdf.bullet_point('Cover requirements: Slabs (25mm), Beams (35mm), Columns (40mm)')
pdf.bullet_point('Minimum reinforcement percentages')
pdf.bullet_point('Development lengths and anchorage')

pdf.section_title('3.3 Steel Structure Design')
pdf.body_text('Steel construction considerations:')
pdf.bullet_point('Steel grades: S275, S355, S460')
pdf.bullet_point('Connection types: Bolted, Welded, Riveted')
pdf.bullet_point('Fire protection requirements')
pdf.bullet_point('Corrosion protection (galvanizing, painting)')
pdf.bullet_point('Composite construction (steel + concrete)')

# Section 4: Electrical Systems
pdf.add_page()
pdf.chapter_title('4. ELECTRICAL SYSTEMS & INSTALLATIONS', 255, 153, 0)

pdf.section_title('4.1 Power Distribution System')
pdf.draw_box_diagram('POWER DISTRIBUTION HIERARCHY', [
    'HV INCOMING (11kV/33kV) → TRANSFORMER',
    '→ MAIN DISTRIBUTION BOARD (MDB)',
    '→ SUB-DISTRIBUTION BOARDS (SDB)',
    '→ FINAL DISTRIBUTION BOARDS (FDB)',
    '→ CONSUMER UNITS (CU) → CIRCUITS → LOADS'
])

pdf.section_title('4.2 Electrical Load Estimation')
pdf.body_text('Typical load allowances per building type:')
pdf.bullet_point('Residential: 30-50 W/m² for general lighting and power')
pdf.bullet_point('Commercial offices: 60-100 W/m²')
pdf.bullet_point('Industrial: 100-200 W/m² (depending on process)')
pdf.bullet_point('HVAC loads: Additional 30-60 W/m²')
pdf.bullet_point('Diversity factors: 0.6-0.8 for residential, 0.7-0.9 commercial')

pdf.section_title('4.3 Safety Systems')
pdf.body_text('Mandatory safety installations:')
pdf.bullet_point('Emergency lighting (maintained/non-maintained)')
pdf.bullet_point('Fire alarm systems (addressable/conventional)')
pdf.bullet_point('Lightning protection systems')
pdf.bullet_point('Earthing and bonding (TN-S, TN-C-S, TT systems)')
pdf.bullet_point('RCD protection (30mA for sockets, 100mA for sub-mains)')

# Section 5: Mechanical Systems
pdf.add_page()
pdf.chapter_title('5. MECHANICAL SYSTEMS (HVAC & PLUMBING)', 102, 51, 153)

pdf.section_title('5.1 HVAC System Types')
pdf.draw_box_diagram('HVAC SYSTEM SELECTION', [
    '1. SPLIT AC: Small spaces (1-5 TR), individual control',
    '2. VRF/VRV SYSTEM: Medium-large buildings, zone control',
    '3. CHILLED WATER SYSTEM: Large buildings, central plant',
    '4. DX SYSTEM: Direct expansion, rooftop units',
    '5. EVAPORATIVE COOLING: Dry climates, energy efficient',
    '6. NATURAL VENTILATION: Passive cooling strategy'
])

pdf.section_title('5.2 Plumbing Systems')
pdf.body_text('Water supply and drainage systems:')
pdf.bullet_point('Cold water: Direct supply or storage tank system')
pdf.bullet_point('Hot water: Central boiler, individual heaters, solar thermal')
pdf.bullet_point('Drainage: Soil stack, waste stack, vent stack systems')
pdf.bullet_point('Rainwater harvesting and grey water recycling')
pdf.bullet_point('Pipe materials: PPR, Copper, HDPE, Cast iron, uPVC')

pdf.section_title('5.3 Fire Protection Systems')
pdf.body_text('Active fire protection installations:')
pdf.bullet_point('Sprinkler systems (wet, dry, pre-action, deluge)')
pdf.bullet_point('Standpipe and hose reel systems')
pdf.bullet_point('Fire pumps and water storage tanks')
pdf.bullet_point('Gas suppression systems (FM200, CO2, Inergen)')
pdf.bullet_point('Smoke control and pressurization systems')

# Section 6: Building Construction
pdf.add_page()
pdf.chapter_title('6. BUILDING CONSTRUCTION METHODS', 0, 128, 0)

pdf.section_title('6.1 Construction Sequence')
pdf.draw_box_diagram('CONSTRUCTION WORKFLOW', [
    '1. MOBILIZATION & SITE SETUP',
    '2. EXCAVATION & FOUNDATION WORKS',
    '3. SUBSTRUCTURE (Basement, Foundation walls)',
    '4. SUPERSTRUCTURE (Columns, Beams, Slabs)',
    '5. BUILDING ENVELOPE (Walls, Roof, Windows)',
    '6. MEP FIRST FIX (Conduits, Ducts, Pipes)',
    '7. INTERNAL FINISHES (Plastering, Painting, Flooring)',
    '8. MEP SECOND FIX (Fixtures, Fittings)',
    '9. EXTERNAL WORKS (Landscaping, Roads)',
    '10. COMMISSIONING & HANDOVER'
])

pdf.section_title('6.2 Construction Techniques')
pdf.body_text('Modern construction methods:')
pdf.bullet_point('Cast-in-place concrete (traditional formwork)')
pdf.bullet_point('Precast concrete elements (columns, beams, slabs)')
pdf.bullet_point('Steel frame construction')
pdf.bullet_point('Composite construction (steel + concrete)')
pdf.bullet_point('Prefabricated/modular construction')
pdf.bullet_point('3D printing in construction (emerging technology)')

pdf.section_title('6.3 Quality Control')
pdf.body_text('Quality assurance measures:')
pdf.bullet_point('Material testing: Concrete cubes (7/28 day strength)')
pdf.bullet_point('Steel reinforcement checks and approvals')
pdf.bullet_point('Formwork inspection before concreting')
pdf.bullet_point('Waterproofing integrity testing')
pdf.bullet_point('Non-destructive testing (ultrasonic, rebound hammer)')

# Section 7: Construction Management
pdf.add_page()
pdf.chapter_title('7. CONSTRUCTION MANAGEMENT & QUALITY CONTROL', 204, 0, 102)

pdf.section_title('7.1 Project Delivery Methods')
pdf.draw_box_diagram('PROCUREMENT ROUTES', [
    '1. DESIGN-BID-BUILD (Traditional): Complete design then tender',
    '2. DESIGN & BUILD: Single contractor responsible for both',
    '3. MANAGEMENT CONTRACTING: Client appoints management contractor',
    '4. CONSTRUCTION MANAGEMENT: Client contracts directly with trade contractors',
    '5. PPP/PFI: Public-Private Partnership for large projects'
])

pdf.section_title('7.2 Construction Scheduling')
pdf.body_text('Scheduling techniques and tools:')
pdf.bullet_point('Gantt charts for timeline visualization')
pdf.bullet_point('Critical Path Method (CPM) for complex projects')
pdf.bullet_point('Program Evaluation and Review Technique (PERT)')
pdf.bullet_point('Resource leveling and allocation')
pdf.bullet_point('Milestone tracking and progress reporting')

pdf.section_title('7.3 Cost Management')
pdf.body_text('Cost control measures:')
pdf.bullet_point('Bill of Quantities (BOQ) preparation')
pdf.bullet_point('Cost estimation methods (preliminary, detailed)')
pdf.bullet_point('Value engineering workshops')
pdf.bullet_point('Variation order management')
pdf.bullet_point('Cost reporting and forecasting')

# Section 8: Building Codes
pdf.add_page()
pdf.chapter_title('8. BUILDING CODES & REGULATIONS', 255, 0, 0)

pdf.section_title('8.1 Nigerian Building Regulations')
pdf.body_text('Key regulatory requirements:')
pdf.bullet_point('National Building Code (NBC) compliance')
pdf.bullet_point('Lagos State Building Control Agency (LASBCA) regulations')
pdf.bullet_point('Development permits and planning approvals')
pdf.bullet_point('Fire safety certification')
pdf.bullet_point('Environmental Impact Assessment (EIA) for large projects')

pdf.section_title('8.2 International Standards')
pdf.body_text('Relevant international codes:')
pdf.bullet_point('British Standards (BS) - commonly used in Nigeria')
pdf.bullet_point('Eurocodes (EC) - European structural design standards')
pdf.bullet_point('American Standards (ASTM, ACI, AISC)')
pdf.bullet_point('International Building Code (IBC)')
pdf.bullet_point('ISO standards for quality management')

# Section 9: Materials
pdf.add_page()
pdf.chapter_title('9. MATERIALS & SPECIFICATIONS', 102, 102, 102)

pdf.section_title('9.1 Concrete Technology')
pdf.draw_box_diagram('CONCRETE MIX DESIGN PARAMETERS', [
    'CEMENT: OPC, PPC, Rapid Hardening',
    'AGGREGATES: Fine (sand), Coarse (granite/gravel)',
    'WATER: Clean, potable, pH 6-8',
    'ADMIXTURES: Plasticizers, Accelerators, Retarders',
    'W/C RATIO: 0.4-0.6 for structural concrete',
    'MIX RATIOS: 1:2:4 (C20), 1:1.5:3 (C25), 1:1:2 (C30)'
])

pdf.section_title('9.2 Steel and Metals')
pdf.body_text('Common structural metals:')
pdf.bullet_point('Mild steel: General structural applications')
pdf.bullet_point('High tensile steel: Reinforcement bars (rebar)')
pdf.bullet_point('Structural steel: I-beams, channels, angles')
pdf.bullet_point('Aluminum: Window frames, cladding')
pdf.bullet_point('Copper: Electrical wiring, plumbing')

pdf.section_title('9.3 Finishing Materials')
pdf.body_text('Interior and exterior finishes:')
pdf.bullet_point('Flooring: Tiles, marble, granite, wood, carpet')
pdf.bullet_point('Wall finishes: Paint, wallpaper, tiles, cladding')
pdf.bullet_point('Ceiling: Plasterboard, acoustic tiles, PVC')
pdf.bullet_point('Joinery: Doors, windows, cabinets')
pdf.bullet_point('Waterproofing: Bitumen, PVC membranes, liquid applied')

# Section 10: Sustainable Building
pdf.add_page()
pdf.chapter_title('10. SUSTAINABLE & SMART BUILDING PRACTICES', 0, 153, 76)

pdf.section_title('10.1 Green Building Principles')
pdf.body_text('Sustainable design strategies:')
pdf.bullet_point('Energy efficiency: LED lighting, efficient HVAC, insulation')
pdf.bullet_point('Water conservation: Low-flow fixtures, rainwater harvesting')
pdf.bullet_point('Material selection: Recycled content, low VOC, local sourcing')
pdf.bullet_point('Indoor environmental quality: Natural light, ventilation')
pdf.bullet_point('Site sustainability: Brownfield development, green spaces')

pdf.section_title('10.2 Smart Building Technologies')
pdf.draw_box_diagram('SMART BUILDING SYSTEMS', [
    '1. BUILDING MANAGEMENT SYSTEM (BMS): Centralized control',
    '2. IoT SENSORS: Occupancy, temperature, lighting',
    '3. SMART HVAC: Variable speed drives, zone control',
    '4. INTELLIGENT LIGHTING: Daylight harvesting, occupancy sensing',
    '5. SECURITY SYSTEMS: Access control, CCTV, biometrics',
    '6. ENERGY MONITORING: Smart meters, real-time tracking'
])

pdf.section_title('10.3 Certification Systems')
pdf.body_text('Building certification programs:')
pdf.bullet_point('LEED (Leadership in Energy and Environmental Design)')
pdf.bullet_point('BREEAM (Building Research Establishment Environmental Assessment)')
pdf.bullet_point('EDGE (Excellence in Design for Greater Efficiencies)')
pdf.bullet_point('Green Building Council Nigeria (GBCN) standards')

# Final Page - Quick Reference
pdf.add_page()
pdf.chapter_title('QUICK REFERENCE - KEY NUMBERS', 0, 51, 102)
pdf.section_title('Critical Dimensions and Values')
pdf.bullet_point('Minimum ceiling height: 2.4m (residential), 2.7m (commercial)')
pdf.bullet_point('Minimum door width: 0.9m (internal), 1.2m (accessible)')
pdf.bullet_point('Stair riser: 150-175mm, tread: 250-300mm')
pdf.bullet_point('Ramp slope: Maximum 1:12 (8.3%) for accessibility')
pdf.bullet_point('Parking space: 2.5m x 5.0m (standard car)')
pdf.bullet_point('Concrete cover: Slabs 25mm, Beams 35mm, Columns 40mm')
pdf.bullet_point('Rebar grades: 250 N/mm² (mild), 460 N/mm² (high yield)')
pdf.bullet_point('Fire resistance: 30min (residential), 60min (commercial)')
pdf.bullet_point('Electrical: 230V single phase, 415V three phase')
pdf.bullet_point('Water pressure: Minimum 1.5 bar, ideal 2-3 bar')

# Save PDF
output_path = '/home/ubuntu/Building_Construction_Guide.pdf'
pdf.output(output_path)
print(f"PDF created successfully at: {output_path}")
