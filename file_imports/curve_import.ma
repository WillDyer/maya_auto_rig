//Maya ASCII 2024 scene
//Name: curve_import.ma
//Last modified: Tue, Dec 26, 2023 11:57:36 PM
//Codeset: 1252
requires maya "2024";
requires "stereoCamera" "10.0";
requires "mtoa" "5.3.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2024";
fileInfo "version" "2024";
fileInfo "cutIdentifier" "202304191415-7fa20164c6";
fileInfo "osv" "Windows 10 Home v2009 (Build: 19045)";
fileInfo "UUID" "F16BFAF7-4D82-A37F-B7F2-3186F36474AB";
createNode transform -n "ctrl_COG";
	rename -uid "EDBB1CC2-430F-D5F5-3383-CDB157AB7DD0";
createNode nurbsCurve -n "nurbsCircleShape1" -p "ctrl_COG";
	rename -uid "40C93A04-48E3-E726-4CB5-0BB7B74506D5";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		39.180580139160156 2.3991187556276616e-15 -39.180580139160156
		3.3928662796758793e-15 3.3928662796758793e-15 -55.409706115722656
		-39.180580139160156 2.3991187556276616e-15 -39.180580139160156
		-55.409706115722656 1.7588677468528917e-31 -2.8724492368828371e-15
		-39.180580139160156 -2.3991187556276616e-15 39.180580139160156
		-5.5504286029220331e-15 -3.3928662796758793e-15 55.409706115722656
		39.180580139160156 -2.3991187556276616e-15 39.180580139160156
		55.409706115722656 -4.6268393341868491e-31 7.5562021985037427e-15
		39.180580139160156 2.3991187556276616e-15 -39.180580139160156
		3.3928662796758793e-15 3.3928662796758793e-15 -55.409706115722656
		-39.180580139160156 2.3991187556276616e-15 -39.180580139160156
		;
createNode nurbsCurve -n "curveShape1" -p "ctrl_COG";
	rename -uid "37672DFB-4F9A-CE69-8C2E-1E8EBADA7709";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		0 0 55
		-2.5 0 55
		-7.5 0 55
		5.440092820663267e-14 0 72.142860412597656
		7.5 0 55
		2.5 0 55
		0 0 55
		;
createNode transform -n "ctrl_root";
	rename -uid "90152FA6-43E2-0D7E-6836-DA8E8BF2ECCE";
createNode nurbsCurve -n "circle_01" -p "ctrl_root";
	rename -uid "576252B7-430A-F498-D37E-7EA7656EA3F8";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		78.361160278320312 4.7982375112553231e-15 -78.361160278320312
		6.7857325593517585e-15 6.7857325593517585e-15 -110.81941223144531
		-78.361160278320312 4.7982375112553231e-15 -78.361160278320312
		-110.81941223144531 3.5177354937057834e-31 -5.7448984737656743e-15
		-78.361160278320312 -4.7982375112553231e-15 78.361160278320312
		-1.1100857205844066e-14 -6.7857325593517585e-15 110.81941223144531
		78.361160278320312 -4.7982375112553231e-15 78.361160278320312
		110.81941223144531 -9.2536786683736982e-31 1.5112404397007485e-14
		78.361160278320312 4.7982375112553231e-15 -78.361160278320312
		6.7857325593517585e-15 6.7857325593517585e-15 -110.81941223144531
		-78.361160278320312 4.7982375112553231e-15 -78.361160278320312
		;
createNode nurbsCurve -n "arrow_01" -p "ctrl_root";
	rename -uid "C3F1F22B-464B-A03F-75A6-76BF51424C22";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		0 0 -110
		-5 0 -110.28118896484375
		-15 0 -110
		1.0880185641326534e-13 0 -140
		15 0 -110
		5 0 -110.28118896484375
		0 0 -110
		;
createNode nurbsCurve -n "arrow_02" -p "ctrl_root";
	rename -uid "9FCB6244-49AF-220A-B524-D3B30E7AC688";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		-110 0 -4.8849813083506888e-14
		-110.28118896484375 0 5
		-110 0 15
		-140 0 -1.7097434579227411e-13
		-110 0 -15
		-110.28118896484375 0 -5
		-110 0 -4.8849813083506888e-14
		;
createNode nurbsCurve -n "arrow_03" -p "ctrl_root";
	rename -uid "0ECEDE2C-4778-7E9E-150F-87A8F410D6F7";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		-1.6002054282343581e-13 0 110
		5 0 110.28118896484375
		15 0 110
		-3.1246438270994548e-13 0 140
		-15 0 110
		-5 0 110.28118896484375
		-1.6002054282343581e-13 0 110
		;
createNode nurbsCurve -n "arrow_04" -p "ctrl_root";
	rename -uid "71EC3EF0-4A34-4F0B-3591-04B382E19873";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 4 0 no 3
		9 0 0 0 1 2 3 4 4 4
		7
		110 0 -5.7398530373120593e-13
		110.28118896484375 0 -5
		110 0 -15
		140 0 -6.2172489379008766e-13
		110 0 15
		110.28118896484375 0 5
		110 0 -5.7398530373120593e-13
		;
createNode transform -n "ctrl_root_world";
	rename -uid "BC2F2FF5-42B7-D2B6-0D3C-C99AB38E5294";
createNode nurbsCurve -n "ctrl_root_worldShape" -p "ctrl_root_world";
	rename -uid "2075BAEF-491B-D496-75BC-09B1866DB6B7";
	addAttr -ci true -sn "width" -ln "width" -dv 0.10000000149011612 -at "float";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		117.54174041748047 7.1973558433665111e-15 -117.54174041748047
		1.0178598415511164e-14 1.0178598415511164e-14 -166.2291259765625
		-117.54174041748047 7.1973558433665111e-15 -117.54174041748047
		-166.2291259765625 5.2766032405586751e-31 -8.6173472871320378e-15
		-117.54174041748047 -7.1973558433665111e-15 117.54174041748047
		-1.6651285385249626e-14 -1.0178598415511164e-14 166.2291259765625
		117.54174041748047 -7.1973558433665111e-15 117.54174041748047
		166.2291259765625 -1.3880518472758288e-30 2.2668607442544175e-14
		117.54174041748047 7.1973558433665111e-15 -117.54174041748047
		1.0178598415511164e-14 1.0178598415511164e-14 -166.2291259765625
		-117.54174041748047 7.1973558433665111e-15 -117.54174041748047
		;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" -20;
	setAttr ".unw" -20;
	setAttr -av ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
	setAttr ".rtfm" 1;
select -ne :renderPartition;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :standardSurface1;
	setAttr ".bc" -type "float3" 0.40000001 0.40000001 0.40000001 ;
	setAttr ".sr" 0.5;
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -cb on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -cb on ".macc";
	setAttr -cb on ".macd";
	setAttr -cb on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -cb on ".pff";
	setAttr -cb on ".peie";
	setAttr -cb on ".ifp";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -k on ".bls";
	setAttr -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -cb on ".ope";
	setAttr -cb on ".oppf";
	setAttr -cb on ".hbl";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -k on ".w";
	setAttr -k on ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
// End of curve_import.ma
