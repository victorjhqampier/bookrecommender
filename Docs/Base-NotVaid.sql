MERGE (doc:Books {axid:'2las computadoras administracion punto vista ejecutivo 1973 brink2 caxi maquera'}) 
	ON CREATE SET
		doc.title='2Las computadoras y la administración',
		doc.subtitle='El punto de vista del ejecutivo',
		doc.edition='Primera edición',
		doc.released='1973',
		doc.notes='<class 'ast.Break'>',
		doc.content='Introducción y revisión general -- La influencia de las computadoras en las prácticas administrativas -- La influencia de las computadoras en las políticas de organización -- Organización de las actividades de las computadoras -- Administración de las computadoras -- Enfrentamiento al futuro.',
		doc.isbn='',
		doc.views=0,
		doc.reviews=0,
		doc.img='https://i.imgur.com/jFmkeLT.jpg',
		doc.link='javascript:;',
		doc.type='Libro',
		doc.topics='Gestion de lentreprise et services annexes : classer ici les affaires'
MERGE (det:Details{bookid:id(doc)}) 
	ON CREATE SET
		det.axid='2las computadoras administracion punto vista ejecutivo class ast break gestion lentreprise et services annexes classer ici affaires introduccion revision general influencia computadoras practicas administrativas influencia computadoras politicas organizacion organizacion actividades computadoras administracion computadoras enfrentamiento futuro'
MERGE (det)-[:DESCRIBE]->(doc)
MERGE (cla:Clasifications{code:'650.0'}) 
	ON CREATE SET
		cla.name='<class 'ast.Break'>',
		cla.axid='650 0 class ast break'
MERGE (cla)-[:DEWEY]->(doc)
MERGE (peo0:People{axid:'victor z brink2'}) 
	ON CREATE SET
		peo0.surname='Brink2',
		 peo0.name='Victor Z.',
		 peo0.born=''
MERGE (peo0)-[:AUTHOR{rol: 'Autor'}]->(doc)
MERGE (peo1:People{axid:'victor caxi maquera'}) 
	ON CREATE SET
		peo1.surname='Caxi Maquera',
		 peo1.name='Victor',
		 peo1.born=''
MERGE (peo1)-[:AUTHOR{rol: 'Autor'}]->(doc)
MERGE (edi0:Editors{axid:'diana2 mexico d f'}) 
	ON CREATE SET
		edi0.name='Diana2',
		edi0.place='México,
		 D.F.'
MERGE (edi0)-[:EDITED]->(doc)
MERGE (edi1:Editors{axid:'diana2 mexico d f'}) 
	ON CREATE SET
		edi1.name='Diana2',
		edi1.place='México,
		 D.F.'
MERGE (edi1)-[:EDITED]->(doc)
MERGE (exe0:Exemplars{axid:'01850422 650 b83'}) 
	ON CREATE SET
		exe0.library='Biblioteca Municipal - Puno',
		exe0.barcode='01-8504-22',
		exe0.code='650 B83',
		exe0.link='javascript:;',
		exe0.libid='52540'
MERGE (doc)-[:ITEM]->(exe0)
MERGE (exe1:Exemplars{axid:'01850422 650 b83'}) 
	ON CREATE SET
		exe1.library='Biblioteca Municipal - Puno',
		exe1.barcode='01-8504-22',
		exe1.code='650 B83',
		exe1.link='javascript:;',
		exe1.libid='52450'
MERGE (doc)-[:ITEM]->(exe1)
MERGE (ser:Series{axid:'na'}) 
	ON CREATE SET
		ser.title='na'
MERGE (ser)-[:SERIALIZED{number: na}]->(doc) RETURN id(doc) as bookid