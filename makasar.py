import folium

def normal(lat, long):
    osm = folium.Map(
        location=[lat, long],
        zoom_start=10,
        tiles='OpenStreetMap')
    return osm


def lingkaranMerah(lat, long):
    LM = folium.CircleMarker(
        radius=15,
        location=[lat, long],
        popup='<i>Redzone<i>',
        color='crimson',
        fill=True,)
    return LM


def lingkaranBiru(lat, long):
    LB = folium.CircleMarker(
        radius=15,
        location=[lat, long],
        popup='<i>Bluezone<i>',
        color='blue',
        fill=True,)
    return LB


def lingkaranHijau(lat, long):
    LH = folium.CircleMarker(
        radius=15,
        location=[lat, long],
        popup='<i>Greenzone<i>',
        color='green',
        fill=True,)
    return LH

	
m = normal(-5.148298,  119.435022)	
folium.Marker(
    location=[-5.147432,  119.417544],
    popup='Mangkura',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.138860,  119.417977],
    popup='Lajangiru',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.124052,  119.411914],
    popup='Butung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.114419,  119.417688],
    popup='Totaka',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.109530,  119.430102],
    popup='Kaluku Bodoa',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.1011766,  119.446269],
    popup='Tallo',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.103348,  119.453343],
    popup='Parang Loe',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.127628,  119.460599],
    popup='Mamajang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.113708, 119.413535],
    popup='Tamalaba',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.136272, 119.417255],
    popup='pisang utara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.167917, 119.438603],
    popup='Tidung',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.157047, 119.4386831],
    popup='Bua Kana',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)
folium.Marker(
    location=[-5.156106, 119.423098],
    popup='Maricaya Sel',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)
folium.Marker(
    location=[-5.167818, 119.411940],
    popup='Baji Mappakasunggu',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)
folium.Marker(
    location=[-5.141831, 119.452967],
    popup='Karampuang',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)             
folium.Marker(
    location=[-5.133029, 119.405028],
    popup='Selat Makassar',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)    
folium.Marker(
    location=[-5.155939, 119.470946],
    popup='Antang',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)   
folium.Marker(
    location=[-5.088232, 119.481245],
    popup='Bira',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[-5.090968, 119.512488],
    popup='Pai',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[-5.127899, 119.522444],
    popup='Paccerakkang',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.186028, 119.472319],
    popup='Paccinongang',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.204491, 119.529654],
    popup='Sunggumanai',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)
folium.Marker(
    location=[-5.177058,119.417290],
    popup='Moh Tahir',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.136897, 119.492532],
    popup='Unnamed Road',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.136320, 119.491051],
    popup='Makassar',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.171860, 119.391509],
    popup='Tj. Merdeka',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.174595, 119.417945],
    popup='Jongaya',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.187930, 119.426871],
    popup='Parang Tambung',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.187246, 119.440604],
    popup='Mangasa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.189298, 119.452621],
    popup='Gn. Sari',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.176305, 119.465324],
    popup='Bangkala',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.191135, 119.497594],
    popup='Tamangapa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.174061, 119.510771],
    popup='manggala',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.157306, 119.506651],
    popup='Moncongloe Lappara',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.108750, 119.493262],
    popup='Daya',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.111144, 119.494978],
    popup='Kapasa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.123112, 119.460989],
    popup='Lakkang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.083787, 119.502531],
    popup='Bulurokeng',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.127899, 119.465452],
    popup='Pampang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.116615, 119.430433],
    popup='Kaluku Bodoa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.129267, 119.486738],
    popup='Tamalanrea Indah',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.084470, 119.533430],
    popup='Sudiang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.184010, 119.455371],
    popup='Gn.Sari',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.164492, 119.426996],
    popup='Jl.Landak  Baru Lorong 9',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.164086, 119.438172],
    popup='Tidung',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.211083, 119.390781],
    popup='Barombong',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.123875, 119.394760],
    popup='LIcon-lIcon',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.152053, 119.401400],
    popup='Panambungan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.155144, 119.396060],
    popup='Maccini Sombala',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.132788, 119.403133],
    popup='Bulo Gading',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.107180, 119.538051],
    popup='Sudiang Raya',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.074111, 119.4811899],
    popup='Untia',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.110343, 119.482621],
    popup='Kapasa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.143629, 119.454466],
    popup='Karapuang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.138158, 119.458929],
    popup='Panaikang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.171325, 119.450003],
    popup='Kasi-kasi',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.189447, 119.4074313],
    popup='Benteng Somba Opu',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.151152, 119.397818],
    popup='Jalan Metro',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.162376, 119.394382],
    popup='Maccini Sombala',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.157648, 119.411551],
    popup='Mariso',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.135080, 119.437300],
    popup='Karuwisi Utara',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.143629, 119.460646],
    popup='Paropo',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.127899, 119.475752],
    popup='Lakkang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.184318, 119.411551],
    popup='Balang Baru',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.117299, 119.409491],
    popup='Ujung Tanah',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.135080, 119.429060],
    popup='Kec. Makassar',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.136106, 119.416014],
    popup='Ujung Pandang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.174061, 119.428030],
    popup='Mannuruki',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.185344, 119.425284],
    popup='Parang Tambung',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.107724, 119.436613],
    popup='buloa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.142261, 119.454123],
    popup='Karampuang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.118667, 119.509398],
    popup='Daya',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.110802, 119.490172],
    popup='Kapasa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.162435, 119.419790],
    popup='Mamajang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.119009, 119.416701],
    popup='Wajo',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.159700, 119.445540],
    popup='Masale',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.047491, 119.328469],
    popup='Barang Lompo',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.081137, 119.320097],
    popup='Barrang Caddi',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.105004, 119.289206],
    popup='P. Kondingareng',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.125164, 119.343229],
    popup='LIcon-LIcon',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.152861, 119.400564],
    popup='Panambungan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.105330, 119.450346],
    popup='Parang Loe',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.064636, 119.522444],
    popup='Sudiang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.075237, 119.534460],
    popup='Sudiang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.162777, 119.511458],
    popup='Manggala',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.174745, 119.510771],
    popup='Tamangapa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.105337, 119.433502],
    popup='Kaluku Bodoa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(    
    location=[-5.161711, 119.437535],
    popup='Letjen Hertasning',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.1506913, 119.430487],
    popup='Monginsidi Baru',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.150094, 119.428213],
    popup='Mutiara I',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.150724, 119.427934],
    popup='Mutiara II',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.151023, 119.427741],
    popup='Mutiara III',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.151077, 119.427880],
    popup='Mutiara IV',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.151419, 119.427794],
    popup='Mutiara V',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.151088, 119.423406],
    popup='Anuang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.149934, 119.419200],
    popup='Domba',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.149998, 119.415348],
    popup='Merpati',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.127643, 119.430176],
    popup='Kalukuang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.128327, 119.424511],
    popup='Baraya',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.133371, 119.422795],
    popup='Wajo Baru',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.134225, 119.419190],
    popup='Gaddong',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.137217, 119.412752],
    popup='Baru',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.144332, 119.414169],
    popup='Jl. Dr. Sutomo 43-51',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.144696, 119.418246],
    popup='Jl. Sungai Nuri',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.146042, 119.411530],
    popup='Jl. Yosep Latumahina 14',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.146569, 119.418606],
    popup='Lembaga Gerakan Orang Tua As',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.149379, 119.421921],
    popup='Audy Husain dr SpB',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.153055, 119.424002],
    popup='Dealers Toto - Makasar',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.192681, 119.420688],
    popup='Parang Tambung',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.200204, 119.395375],
    popup='Barombong',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.185520, 119.406273],
    popup='Tj. Merdeka',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.083161, 119.540345],
    popup='Sudiang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.113938, 119.412973],
    popup='Tamalabba',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)   
folium.Marker(
	location=[-5.109434, 119.483992],
    popup='Kapasa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)  
folium.Marker(
	location=[-5.120718, 119.469572],
    popup='Parang Loe',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)   
folium.Marker(
	location=[-5.190131, 119.497381],
    popup='Tamangapa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)  
folium.Marker(
	location=[-5.174745, 119.510428],
    popup='Tamangapa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)  
folium.Marker(
	location=[-5.137474, 119.478842],
    popup='Tamalanrea Indah',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)   
folium.Marker(
	location=[-5.183977, 119.399878],
    popup='Tj. Merdeka',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)        
folium.Marker(
	location=[-5.159668, 119.496695],
    popup='ayu agung III',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.158535, 119.495504],
    popup='Batu Raja',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.157520, 119.496051],
    popup='Tj.Pinang jaya',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.156590, 119.493047],
    popup='kutacene 2',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.154944, 119.489828],
    popup='Mentarang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.155190, 119.489077],
    popup='Baruga',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.153630, 119.487360],
    popup='Bunaken',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.153908, 119.487060],
    popup='Takabonerate',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.156430, 119.487478],
    popup='Rinjani',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.153823, 119.485826],
    popup='Kintamani',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1446417,119.4081528],
    popup='Hotel ibis Makassar city center Kecamatan Makassar, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1493299,119.408606],
    popup='Travellers Hotel PhinisiMariso, Kunjung MIcon, Kecamatan Makassar, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1275586,119.4059663],
    popup='Ocean View Hotel Pattunuang, Wajo, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1371364,119.4059031],
    popup='Asston Makassar Hotel & Convention Baru, Ujung Pandang, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)   
folium.Marker(
	location=[-5.1468997,119.412981],
    popup='LARIZ Wthree Hotel Lagaligo Mangkura, Kecamatan Makassar, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)        
folium.Marker(
	location=[-5.1395446,119.411696],
    popup='Hotel Novotel Makassar Grand Shayla Sawerigading, Ujung Pandang, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)    
folium.Marker(
	location=[-5.1407681,119.4078358],
    popup='Hotel Santika Makassar Maloku, Ujung Pandang, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(
	location=[-5.1389774,119.4038936],
    popup='Losari Beach Hotel Makassar Bulo Gading, Ujung Pandang, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)  
folium.Marker(
	location=[-5.1679412,119.4259841],
    popup='Four Points by Sheraton Makassar Banta-BantIconng, Rappocini, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)  
folium.Marker(
	location=[-5.1411782,119.4371453],
    popup='Amaris Hotel Pettarani Sinrijala, Kecamatan Makassar, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.125502, 119.432703],
    popup='lorong 2b la latang tallo,kota makassar',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.122727, 119.430906],
    popup='Suangga',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.129994, 119.433781],
    popup='Karuwisi Utara',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.123946, 119.515771],
    popup='Jl. Lanraki',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.130507, 119.514290],
    popup='Jl. Telkom I',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.129875, 119.5135570],
    popup='Jl. Perumtel III',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.131275, 119.509405],
    popup='Jl. Palapa IV No.90',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.120311, 119.529682],
    popup='Jl. Rudal 4',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.092954, 119.538072],
    popup='Jl. Poros Asrama H.',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.112574, 119.442371],
    popup='Buloa',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1251137,119.4073265],
    popup='Rumah makan Malabar Melayu Baru, Wajo, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)  
folium.Marker(
	location=[-5.150782,119.4197483],
    popup='Rumah makan Muda Mudi Maricaya, Kecamatan Makassar, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(
	location=[-5.1507813,119.4044273],
    popup='Ratu Gurih Seafood Market Resto Losari, Ujung Pandang, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1501277,119.4124008],
    popup='Rumah Makan Nyoto Banta-BantIconng, Rappocini, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1289015,119.4046927],
    popup='Rumah Makan Rajawali Jl Metro Tanjung Bunga',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.6421336,108.6386637],
    popup='New Cendana Masale, Panakkukang, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1362844,119.505475],
    popup='Rumah Makan Nike Ardilla Tamalanrea, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.136931,119.5062053],
    popup='Rumah Makan Kapurung Aroma Palopo Tamalanrea, Makassar, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1279313,119.4168313],
    popup='Rumah Makan Bravo Parang Layang, Bontoala, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.13693,119.4733743],
    popup='Rumah Makan Citra Minang Karampuang, Panakkukang, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
    location=[-5.133116, 119.488026],
    popup='Universitas Hasanuddin',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.139116, 119.522030],
    popup='Perumahan Griya Bumi Firda Mas, B',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.139919, 119.523914],
    popup='Jl. Paccerakkang Paccerakkang, Biring Kanaya, Kota M ',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.141360, 119.521004],
    popup='Masjid Babul KhIconr',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.140949, 119.519689],
    popup='Rental MOBIL BTP',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)   
folium.Marker(
    location=[-5.141141, 119.522731],
    popup='Unnamed Road',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)   
folium.Marker(
    location=[-5.133459, 119.524624],
    popup='Green Mutiara Paccerakkang',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)   
folium.Marker(
    location=[-5.133739, 119.527797],
    popup='Jl. Kotipa XIV',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)   
folium.Marker(
    location=[-5.128536, 119.529795],
    popup='Jl. Bukamata I',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)           
folium.Marker(
    location=[-5.124913, 119.526630],
    popup='Jl. Poros Mangga Tiga',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.150457, 119.469715],
    popup='KSP Makassar Maju',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.150357, 119.469659],
    popup='Alfamidi',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[-5.150319, 119.469723],
    popup='Sinar Warna Photo',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m) 
folium.Marker(
    location=[-5.150392, 119.469417],
    popup='Studio Frame Indonesia',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[-5.150362, 119.469302],
    popup='Uni Salon',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[-5.150283, 119.469381],
    popup='Dr. dr. H. Faridin HP ,Sp .PD –KR',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[-5.150256, 119.469487],
    popup='Pinus Game Center and Cafe',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)  
folium.Marker(
    location=[5.150243, 119.469297],
    popup='DZAKY Jaya Motor',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)    
folium.Marker(
    location=[-5.150335, 119.469163],
    popup='Indah Salon',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)   
folium.Marker(
    location=[-5.150104, 119.469248],
    popup='Warkop DIconng Kanang',
    icon=folium.Icon(icon='info-sign')
     ).add_to(m)
folium.Marker(
	location=[-5.147049,119.4267581],
    popup='Baju Murah di Makassar Mannuruki, Tamalate, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.152259,119.4577043],
    popup='Lucky Bastard Batua, Manggala, Kota Makassar, Sulawesi Selatan',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.152258,119.4248733],
    popup='Distributor Baju Batik Makassar Tamalanrea, Kecamatan Biringkanaya, Makassar',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1522561,119.4248732],
    popup='Konveksi Baju Kaos Makassar Baji Mappakasunggu, Mamajang, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(
	location=[-5.1618342,119.4584947],
    popup='M7 Kaos Polos In Makassar Borong, Manggala, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(
	location=[-5.1618332,119.4256637],
    popup='MIconstro Karate Sport Lette, Mariso, Kota Makassar, Sulawesi Selatan ',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(	
	location=[-5.096051, 119.537276],
    popup='Poros Asrama',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(	
	location=[-5.098669, 119.534540],
    popup='Goa Ria 8',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(	
	location=[-5.099006, 119.534164],
    popup='Pajjaiyyang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.100401, 119.533252],
    popup='Toko Nasatani',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.101785, 119.530967],
    popup='Makassar 1',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.101988, 119.531348],
    popup='Makassar 2',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.101117, 119.531981],
    popup='Maros 1',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.101331, 119.532308],
    popup='Maros 3',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.101684, 119.532496],
    popup='Maros 5',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.102234, 119.532968],
    popup='Maros 7',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.111194, 119.423207],
    popup='Gusung',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(		
	location=[-5.121319, 119.411575],
    popup='Mampu',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.127939, 119.414899],
    popup='Ende',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(		
	location=[-5.131930, 119.413726],
    popup='Pattunuang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(		
	location=[-5.133196, 119.418711],
    popup='Gaddong',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.133001, 119.407372],
    popup='Bulo Gading',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(	 
	location=[-5.127841, 119.437282],
    popup='Tammua',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.134948, 119.427996],
    popup='Malimongan Baru',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m) 
folium.Marker(		
	location=[-5.128425, 119.415876],
    popup='Bontoala Parang',
    icon=folium.Icon(icon='info-sign')
    ).add_to(m)
folium.Marker(		
	location=[-5.125797, 119.408643],
    popup='Melayu Baru',
    icon=folium.Icon(icon='info-sign')
	).add_to(m) 
lingkaranMerah(-5.1522561,119.4248732).add_to(m)
lingkaranBiru(-5.138860,  119.417977).add_to(m)
lingkaranBiru(-5.114419,  119.417688).add_to(m)
lingkaranBiru(-5.109530,  119.430102).add_to(m)
lingkaranBiru(-5.186028, 119.472319).add_to(m)
lingkaranBiru(-5.167917, 119.438603).add_to(m)
lingkaranBiru(-5.096051, 119.537276).add_to(m)
lingkaranHijau(-5.099006, 119.534164).add_to(m)
lingkaranHijau(-5.1679412,119.4259841).add_to(m)
lingkaranHijau(-5.125797, 119.408643).add_to(m)
lingkaranMerah(-5.128425, 119.415876).add_to(m)
lingkaranMerah(-5.134948, 119.427996).add_to(m)
lingkaranMerah(-5.127841, 119.437282).add_to(m)
lingkaranMerah(-5.133001, 119.407372).add_to(m)
lingkaranBiru(-5.133196, 119.418711).add_to(m)
lingkaranBiru(-5.131930, 119.413726).add_to(m)
lingkaranBiru(-5.127939, 119.414899).add_to(m)
lingkaranHijau(-5.121319, 119.411575).add_to(m)
lingkaranHijau(-5.111194, 119.423207).add_to(m)
lingkaranHijau(-5.102234, 119.532968).add_to(m)
lingkaranHijau(-5.101331, 119.532308).add_to(m)
lingkaranHijau(-5.100401, 119.533252).add_to(m)
lingkaranBiru(-5.099006, 119.534164).add_to(m)
m.save('index.html')
