import sql_generator
import inputs

print(inputs.isSanatized("\",\"\"); DROP TABLE PRISPEVEK; --" ) )

name = inputs.nonEmptyStringInput("Napis jmeno")
text = inputs.nonEmptyStringInput("Napis text")

print(sql_generator.genrateInsert(name,text))