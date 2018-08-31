import rdflib
from rdflib.plugins.sparql.results.csvresults import CSVResultSerializer
from textwrap import dedent

g = rdflib.Graph()
g.parse('test1.owl')

query = dedent("""
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl:  <http://www.w3.org/2002/07/owl#>
PREFIX BIO:  <http://www.purl.obolibrary.org/BIO/>

SELECT ?class ?classLabel
WHERE {
    ?class rdfs:label ?classLabel .
    ?has_filling rdfs:label "has filling" .
    ?saline_filling rdfs:label "saline filling" .

    ?class rdfs:subClassOf ?restriction .
    ?restriction owl:onProperty ?has_filling;
                 owl:someValuesFrom ?saline_filling .
}
""")

qres = g.query(query)

csv = CSVResultSerializer(qres)
with open("queryresults.csv", "wb") as file:
        csv.serialize(file)
