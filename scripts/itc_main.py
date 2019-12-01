# DONEs
#1 - escolher o dataset (da pasta itc/datasets/txt/"nome_do_dataset")
# 2 - rodar o dataseter na pasta itc/datasets/html/"nome_do_dataset", que vao jogar os resultados em datasets/txt/"nome_do_dataset"
# 3 - alimentar os arquivos .txt da pasta no modelo
# 4 - criar uma nova string de acordes com alguma seed de uma lista pré feita
# 5 - decodificar o resultado usando o chordDecoder
# 6 - retornar o arquivo na pasta itc/resultados

import os, dataseter, Model, chord_decoder, music21

print('--------------------')
options = os.listdir('../datasets')
for i in options:
    print(i)
print('--------------------')

dataset_path = str('../datasets/' + input('Escolha seu dataset dentre os listados acima: ') + '/')

print('--------------------')

if(len(os.listdir(dataset_path)) > 2):
    options = os.listdir(dataset_path)
    for i in options:
        if i != 'html' and i != 'txt':
            print(i)
    print('--------------------')
    change = input('Deseja mudar para algum dos datasets mais específicos acima? (s/n): ')
    if change == 's':
        dataset_path += (input('Digite o nome do dataset desejado: ') + '/')
    print('--------------------')

dataseter.html_to_txt(dataset_path)
content = Model.modeler(dataset_path+"txt/")

print(content)

output = chord_decoder.decodificarCifra(content)

output_files = os.listdir("../outputs/")

file_number = len(output_files) + 1

chord_decoder.newMusicXMLFile(output, "../outputs/output"+str(file_number))

print("Output decodificado com sucesso")