from ... import bl_info
from ... preferences import get_preferences

'''
Make sure to have 2 or more items per list item.
'''


# Screen Saver Tips
tips = [
    ["Sharpen / Csharp", "Ctrl + click to apply booleans!", "Also performs sharpening", "Part of sharpen"],
    ["Settings >> Shade Solid", "Shift + Click to duplicate and make solid", "Read the tooltip"],
    ["BoolShift", "Select a boolshape and press Q", "Shift a bool to any state from any state."],
    ["To_Shape V2", "Q >> O >> T ", "Quick access w/to_shape V2", "Allows for the creation of a shape in the area of a selection", "Decap allows for various interesting possibities"],
    ["Q >> Add Modifiers >> Cloth", "Convert a selection to cloth", "Adjust pressure in the cloth panel", "Adjust the shrinkage amount as well.", "Optimized for single sided geometry"],
    ["Spherecast", "Q >> Meshtools >> Spherecast", "Converts a box into a sphere.","Adds a subdivision then cast modifier."],
    ["Bevel", "1 - Resets bevel to edge bevel defaults (profile 0.5)", "2 - Sets bevel to vert bevel defaults (profile 0.5)", "3 - Allows for a profile 1.0 bevel w/ edge. Useful for subdivision conversion"],
    ["Array V2", "Press V for 3d array", "Allows for a more interactive way to set the distance and segments at once."],
    ["LookDev +", "Alt + V >> V", "Press R in modal to set the environment to the render."],
    ["Subdivison", "Q >> Add Modifier >> Subdivision", "Alt + Click to set it first in the stack", "Can be assistive with upresing boolean geometry."],
    ["Taper", "Q >> Meshtools >> Taper", "Shift + clicking allows for individual tapering of multiple objects.", "Useful for tapering boolshapes post boxcutting. Supports Wedge"],
    ["Dice", "Ctrl + Click to dice on all axis'", "Alt + click to smart apply unto dice.","Pressing T allows for Twist to be used post dice"],
    ["Stacking Bevels", "Ctrl + click to add a 30 degree bevel ", "Ctrl + shift click to add a 60 degree bevel", "Q >> Operations >> Step will also add a 60 degree bevel in non-destructive mode."],
    ["Smart Shapes", "Activate Hopstool using the T Panel button", "The topbar has a plethora of smart shapes to choose from", "Hold ctrl to view dots and adjust shapes dynamically."],
    ["Manage", "Unify - bring all solid objects into the active collection", "Sync - ensure render settings are the exact same as viewport", "Evict - remove cutters and evict cutters to the Cutters collection", "Purify - Delete all cutters unassociated with meshes. But keep extractions"],
    ["Smooth", "Shift + click to create a smart vgroup for omission", "Allows for mirrored smoothing", "Ideal for hard surface smoothing"],
    ["New Modifier", "Ctrl + click any modifier to add a new modifier", ],
    ["UV Display", "Q >> O >> U", "Display UVs on the fly. In the 3d view!", "Auto UV under Q >> Meshtools >> Auto UV also displays UVs"],
    ["Mark ", "Edit Mode Q >> Mark", "Without selection mark performs an ssharpen operation "],
    ["Up to date? ", "The hops button at the top of the 3d view will tell you ", "Icons are also available for the marketplace of your choosing ","Get updated!"],
    ["Accushape ", "Located in Q >> Operations", "Also at the top of hopstool >> Alt + W ", "Allows for interactive scaling and proportion adjustments of objects"],
    ["Radial Array ", "For single axis mirroring you use mirror (alt + X)", "For radial mirroring, radial array is recommended "],
    ["Sculpt Quick Jump ", "Q >> Operations >> Brush ", "Displays a brush window for quick selection ", "Now supports cloth filter"],
    ["Multi Axial Dice ", "Q >> Meshtools >> Dice (ctrl + click)", "Ctrl + clicking Dice will dice on all axis ", "Dice can be used as a remesher of sorts this way"],
    ["UV Display ", "Q >> O >> U ", "Displays uvs in the 3d view. "],
    ["Link Ops >> Pizza Ops", "Ever order a pizza?", "Q >> Settings >> Link Ops (ctrl + click)", "AR hates it but it's a classic"],
    [f"HardOPS Version: {bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}.{bl_info['version'][3]}", f"Service Pack Level: {bl_info['version'][3]}"],
    ["Tips V1", "This is still a concept", "Thanks for reading my tips"],
    ["Boolean Grates", "HOPStool grid shapes can be shift clicked to conform to a boolshape", "Try it out!"],
    ["Everyscroll Autoscroll", "Shift + Space during everscroll autoscrolls", "Give your middle mouse button a break"],
    ["UV Display Edit Mode", "Still Q O U", "Now displays the whole uv set while coloring the selection"],
    ["Really like smart apply?", "Sharpen prefs allow it to be mapped now", "Try the successor of Csharpen!"],
    ["Dice Join", "When using dice / twist w/ multiple objects they now apply and join", "This should help deform that multiselection"],
    ["Pong", "Ctrl + Click about in settings to play pong!", "Now displaying ads from the Link Launcher"],
    ["Uniquify", "Now supporting curve cases", "It just gets better and better."],
    ["Selection To Bool V3", "Located in ST3 tools / edit mode", "Turn a face to a boolean. Now better than ever."],
    ["Polygon Debug", "Now at the topbar of hopstool", "Get in and solve that topology!"],
    ["Array V2", "Deadzone Circle - allows for adjustment without changing position", "Shows on the launch of array V2"],
    ["Uniquify", "Now supporting radial arrays", "Give it a try!"],
    ["Curve Alot of Stuff?", "Theres a Q menu option for that", "Use F9 to scroll and find the perfect axis"],
    ["3d Cursor Alignment", "Ever tried to align the 3d cursor to an edge / face?", "Edit Mode Q > O > S will take care of you."],
    ["Inset Slice", "Inset is cool and all but have you tried inset slice?", "It can be found in the F9 panel of inset"],
    ["Meshclean Editmode", "Start in editmode", "Finish in edit mode."],
    ["Taper / Wedge", "You've seen it in boxcutter.", "Now in hops under Q >> Meshtools."],
    ["To_Shape 1.5", "Miss individual orientation with to_shape?", "1.5 is available under opt-ins and has your back."],
    ["Cut In / Merge", "Merge is part of cut_in. Read the tooltip", "Cut / Slice and Intersect all at the same time."],
    ["Select Tool Quad / Tri Support", "Select tool can make quads and tris on the fly if you read the help", "F is also there for making faces and filling them"],
    ["Everscroll", "Modifiers, Boolshapes and Children.", "Scroll em all and be sure to try shift + space to autoscroll!"],
    ["ZenUV", "Shoutout to ZenUV for their requests improving UV Display", "Now supporting Zen UV via HOPSlink!"],
    ["Blank Materials", "Generates a random material", "Be sure the read the tooltip. It does alot"],
    ["Blank Camera", "When used adds a camera to view in addition to making a marker in the timeline", "Set up shots and pan quick and easy"],
    ["Blank Lights", "Don't know what kinda lighting rig to use?", "We'll show you endless possibilities"],
    ["Material Replacement w/ Scroll", "Alt + M >> Shift + click material scroll", "Keep the material but replace the nodes."],
    ["Blank Material Scroll", "Ctrl + click blank material to scroll endless blank materials", "Try it with a selection!"],
    ["Blank Light Non-Destructive Scroll", "Alt + V >> Ctrl + click Blank Light", "Keep the rig and lights but see endless choices"],
    ["Blank Light - Expanded Mode", "Tab in blank light will open a light editor", "Customize, Isolate and refine the ultimate lighting setup"],
    ["Light Rig Reuse", "Shift + S in Blank Light allows for rig to be saved", "And with J the configurations saved can be cycled."],
    ["Looking for tutorials?", "Q >> Settings >> Link Ops", "From this window users can scroll and find whatever they need"],
    ["HOPS Button", "At the top of the 3d view is the HopsButton", "Links are the final tab and can help you with docs or tutorials."],
    ["Boxcutter", "New to boxcutter?", "N panel displays help and hotkeys. Useful for beginners"],
    ["Material Scroll", "Shift + Click - Non-destructive scroll (replace the nodes / keep the mat)", "Ctrl + Click - Blank Material Scroll (unique material per scroll)"],
    ["Manage - Collect","Collect - Unify all solid objects into a reusable collection prime for reuse with PowerLink!", "Available in the F6 "]
]