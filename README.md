# Traveling-Salesman-Problem 💼

<div style="display: inline-block;">
<img align="center" height="20px" width="60px" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> 
<img align="center" height="20px" width="80px" src="https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg"/> 
<a href="https://github.com/ohenriquesouza">
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"/>
</a> 
</div>

</hr>

# OBJETIVOS

<p align="justify">⠀⠀⠀⠀Foi proposto pelo professor <a href="https://github.com/mpiress">Michel Pires da Silva</a>, na disciplina de Algoritmos e Estruturas de Dados II no CEFET-MG campus V no começo do mês de Novembro (2022), uma atividade em dupla na qual os alunos deveriam escolher qualquer problema real para resolve-los utilizando a estrutura dos grafos. Para tal, ficou livre para que as duplas escolhessem em qual linguagem iriam optar para a solução do problema. As linguagens disponíveis eram: <i>C, C++ e Python</i>. Para este trabalho, a dupla optou por desenvolver todo problema na linguagem <b>Python</b>, visando mais "simplicidade" para que a estrutura estudada fosse implementada. Outro fator que influênciou a escolha de determinada linguagem de programação foi que, em Python, com auxílio de bibliotecas externas, torna-se possível gerar uma imagem, facilitando a visualização do grafo.</p>

# INTRODUÇÃO

<p align="justify">⠀⠀⠀⠀Antes de desenvovler qualquer tipo de resenha sobre os problemas computacionais e as estruturas que serviram de base para a realização do trabalho, antes deve-se apresentar o conceito por trás dos <b>Grafos [ I ]</b>. A teoria dos grafos é um ramo da matemática, o qual estuda as relações entre os objetos de um determinado conjunto. Para que seja possível, são utilizadas estruturas chamadas de grafos, <i> <b>G (V, E)</b> </i>, onde <i><b>"V"</b></i> é um conjunto não vazio de objetos chamados de vértices,  e <i><b>"E"</b></i> (que vem do inglês edges), é um subconjunto de pares não ordenados dos vértices V. </p>

<p align="justify">⠀⠀⠀⠀Certo, mas de onde veio essa teoria? Bem, para discutir sobre a origem dos grafos, é necessário voltar até o ano de 1736, onde o matemático suíço Leonhard Paul Euler ( 1707 -  1783 ), publicou um artigo sobre o Problema das Sete Pontes de Königsberg (que é considerado o primeiro resultado da teoria dos grafos). O problema é baseado na cidade de Königsberg (Kaliningrado), que é cortada pelo Rio Prégolia, onde há duas grandes ilhas, que juntas, formam um complexo que na época continha sete pontes. Discuita-se nas ruas a possibilidade de se atravessar todas as pontes, passando por todas as cidades, sem que fosse necessário passar pela mesma ponte mais de uma vez.</p><br/>

<center>
<img src="imgs/pontes.jpg" width=400px><br/>
<i>Figura I: Representação gráfica de um mapa representante do problema das sete pontes;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Após esta simplória introdução ao tema, é esperado que o leitor tenha entendido que se é pode tentar visualizar de maneira "física", um grafo de inúmeras formas. Abaixo, segue um modelo genérico sobre a "aparência" de um grafo simples.</p><br/>

<center>
<img src="imgs/graph1.png" width=400px><br/>
<i>Figura II: representação de um grafo simples;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Existem duas definições quando se trata deste tipo de estrutura: os Grafos e os Dígrafos. Em literatura, as definições básicas sobre essas estruturas são ditas da seguinte maneira:</p>

<center><b><i>Dígrafos</b></i> (grafos direcionados)</center>
<ul>
    <li>Compostos por um conjunto <b>V</b> de vértices;</li>
    <li>Outro conjunto <b>E</b> de arestas;</li>
    <li>Uma estrutura de "mapa" <b>s, t</b> ➝ <b>V</b>, onde "s" é a origem (E) e "t" é o destino (E);</li>
</ul>

<center><b><i>Grafos</b></i> (grafos não direcionados)</center>
<ul>
    <li>Compostos por um conjunto <b>V</b> de vértices;</li>
    <li>Outro conjunto <b>E</b> de arestas;</li>
    <li>Uma função <b>w : E</b> ➝ <b>P ( V )</b>, que associa a cada aresta um sbconjunto de dois ou de apenas um elemento de vértices, interpretado como os pontos terminais da aresta.</li>
</ul>

<p align="justify"><b>OBS:</b> Um grafo direcionado ou não, que possui pesos nas arestas, uma função adicional <b>E ➝ R</b> realiza essa associação [aresta-valor]. Este modelo de grafos aparece em problemas de melhor rota tal como o <b>Problema do Caixeiro Viajante [ II ]</b>, próximo tópico que será abordado neste estudo.</p>

<p align="justify">⠀⠀⠀⠀Muito famoso e discutido dentro da área matemático-computacional, o Problema do Caixeiro Viajante é um problema que tenta determinar a menor rota para percorrer uma série de cidades e retornar a cidade de origem. Ele se mostra muito importante e essêncial, o qual deve fazer parte da bagagem de todo profissional competente na área. Em literatua, enuncia-o da seguinte forma:</p>

<p align="jusitfy">"<i>Suponha que um caixeiro viajante tenha de visitar '<b>n</b>' cidades diferentes, iniciando e encerrando sua viagem na primeira cidade. Suponha, também, que não importa a ordem com que as cidades são visitadas e que de cada uma delas pode-se ir diretamente a qualquer outra.
O problema do caixeiro viajante consiste em descobrir a rota que torna mínima a viagem total.</i>"</p>

<p align="justify">⠀⠀⠀⠀Para exemplificar o enunciado do problema, temporáriamente, atribui-se 4 ao número '<b>n</b>' de cidades pelas quais o caixeiro deve passar. Cada cidade é represetada por um número inteiro e positivo: '<b>1</b>' para a primeira cidade, '<b>2</b>' para a segunda cidade e assim por diante. Uma rota que o caixeiro poderia consiederar seria: <i>saia de 1 e vá para 2, dessa vá para 3 e caminhe para 4, por fim, retorne a 1,</i> dessa forma, fazendo o caminho 1-2-3-4-1. O problema do caixeiro é um clássico na área de problemas de otimização combinatória e é um problema da classes dos <b>NP-Difícil</b>. Ao se resolver um problema deste tipo, deve-se antes tentar reduzilo a um problema de enumeração: encontrar todas as possíveis rotas e calcular o comprimento de cada uma delas, dessa forma, vendo qual a menor.</p><br/>

<center>
<img src="imgs/caixeirov.gif" width=400px><br/>
<i>Figura III: representação de um grafo do Problema do Caixeiro Viajante;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Antes de introduzir o problema no qual o trabalho será desenvolvido, é importante apresentar alguns outros conceitos essênciais para que o mesmo possa ser compreendido. Falando em caminhamento sob um grafo no qual cada vértice apenas pode ser visitado uma vez, fala-se de um conceito chamado <b>Caminho Hamiltoniano [ III ]</b>. Um caminho hamiltoniano é aquele que permite passar por todos os vértices de um grafo G, entretanto, sem repetir nenhum deles, ou seja, caminho hamiltoniano diz respeito aquele pelo qual, dado um caminho, todos os vértices serão visistados e nenhum será repetido. Neste estudo, o caminho a ser percorrido dentro do grafo pode facilmenter ser tratado como um ciclo, e por conta disso, o problema aqui tratado se encaixa perfeitamente como um ciclo hamiltoniano, como será entendido a diante no documento.</p>

<p align="justify">⠀⠀⠀⠀Outro conceito relevante para levar a um entendimento satisfatório do trabalho aqui documento, é sobre os algoritmos gulosos e como seu comportamente influencia um programa a encontrar sua melhor solução (ou quase). Neste tipo de método, os algortimos, durante seu processo de tomadas de decições, sempre optam por aquela que parece ser a melhor opção local. Isso implica que, em todos os casos, as escolhas serão tomadas apenas se baseando na melhor opção no momento da análise, sem "pensar" se tal escolha, trará a melhor solução global ao fim de sua execução. Pensando em algoritmos gulosos, é necessário aceitar que a decição tomada é sempre a melhor, e que um conjunto dessas, o levará a melhor solução possível para o problema.<br/>⠀⠀⠀⠀Muitas das vezes, esse comportamento dito "guloso" o leva para a melhor solição do problema, apesar de não ser sempre, o abismo que existe em termos de facilidade durante a implementação de um algoritmo deste tipo, com algoritmos de programação dinâmica, os fazem serem escolhidos diversas vezes. Por fim, o último conceito que deve ser apresentado antes de dar início a explicação do trabalho é sobre o método de busca DFS, do inglês <i>Deep First Search</i>, ou "Busca em Profundidade" é um algoritmo usado para realizar uma busca ou travessia em alguma estrutura de dados, como: árvore, substrutura de árvores e/ou grafos.</p>


<p align="justify">⠀⠀⠀⠀Com a teoria dos grafos e o Problema do Caixeiro Viajante já pré-estabelecidos, pode-se começar a discução sobre como esses dois tópicos da computação foram utilizados para a solução do problema proposto. Para este estudo, um engenheiro elétrico residente de Divinópolis que atende clientes em 9 diferentes cidades, busca a melhor rota correlacionando o tempo de trabalho que um cliente residente da cidade ' x ' irá exigir, com o ganho que terá por trabalhar para ele. É importante ressaltar que, como dito, os clientes estão espalhados pelas 9 cidades em torno de Divinópolis, entretanto, em uma semana, devido a carga horária disponível para aquela, nem todas as cidades serão sempre visitadas pelo engenheiro. Visando evitar prejuízo, o caminho pelo qual será percorrido para prestar seu serviço deve ser minuciosamente calculado. Afinal, cada semana terá uma carga horária diferente a ser comprida, portanto, o maior valor em dinheiro deve ser convertido a partir desta limitação horária.</p>
<p align="justify">⠀⠀⠀⠀Este mapa da região Centro-Oeste de Minas Gerais demarca todas as cidades onde os clientes moram/trabalham, bem como define Divinópolis como sendo a origem e destino final, ou seja, torna-se um ciclo hamiltoniano com algumas alterações, uma vez que, a partir da carga horária disponível, nem todas as cidades poderão ser visitadas, uma vez que, ao fim do dia, o engenheiro deve retornar a Divinópolis para que possa voltar até sua casa (sem que exceda a carga horária daquele dia de serviço).</p><br/>

<center>
<img src="imgs/zoomwithmarks.png" width=550px><br/>
<i>Figura IV: região de atuação para o estudo, partindo de Divinópolis;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Com o auxílio das bibliotecas externas: <i><b>matplotlib [ III ], numpy [ IV ], scipy [ V ] </b>e do pacote <b>NetWorkX [ VI ] </i></b>, a partir da organização das coordenadas (o que será mostrado mais a diante do trabalho), tornou-se possível visualizar a estrutura do grafo na qual o algoritmo irá trabalhar encima. Percebe-se que o grafo apresenta uma estrutura muito satisfatória, uma vez que é possível compara-lo e perceber as semelhanças com o mapa de Minas Gerais.</p><br/>

<center>
<img src="imgs/graphimg.jpg" width=450px><br/>
<i>Figura V: grafo gerado a partir do mapa de Minas Gerais presente na Figura IV;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Ademais, vale reforçar a importância de levar em consideração não apenas o tempo de deslocamento para sair de uma cidade ' x ' e chegar em ' y ', mas também o gasto de combustível ao final do dia. Se tratando de trabalho, o ganho oriundo do serviço prestado para os clientes, deve ser capaz de suprir os gastos do combustível, bem como gerar lucro. Visando maximizar a otimização do uso do tempo/combustível, algumas regras são criadas referentes as visitas em algumas certas cidades. Para que o engenheiro possa ir trabalhar em Bom Despacho, por exemplo, ele deve, obrigatóriamente, trabalhar antes ou em Nova Serrana, ou em Lagoa da Prata, uma vez que não é possível chegar a Bom Despacho sem antes passar por estas cidades. Essa situação acontece novamente quando o engenheiro precisa prestar serviço na cidade de Oliveira. Para chegar ao seu destino, ele deve antes passar e trabalhar em Cláudio primeiro, uma vez que estão no "mesmo" caminho.</p>

<p align="justify">⠀⠀⠀⠀Por conta disso, o consumo do carro utilizado para o transporte durante as viagens a trabalho é importante e tem papel fundamental na construção do grafo, juntamente com o tempo gasto durante o deslocamento. Para tal, foi construida a seguinte tabela contendo todas as informações necessárias para a construção e organização do grafo. O carro utilizado para realizar o transporte até as cidades é um <i>Ford Ka S. (sedan) 1.5</i> de ano 2015, o modelo apresenta consumo médio em vias rodoviárias de ± 13,6 Km/L segundo o site <b>carrosnaweb [ VII ]</b>.</p><br/>

| Percurso               |  Distância                         |  Tempo       | Consumo    |       
| :-----------------------:| :-----------------------------------:|:--------------:|:------------:|
|  <i>Divinópolis ➝ Nova Serrana</i>        | 44,8 Km                            |0,75 h        |3,29 L      |
|  <i>Divinópolis ➝ Sete Lagoas</i>        | 180,3 Km                           |2,93 h        |13,25 L     |
|  <i>Divinópolis ➝ Belo Horizonte</i>        | 127,8 Km                           |2,13 h        |9,39 L      |
|  <i>Divinópolis ➝ Ouro Preto</i>        | 209,4 Km                           |3,38 h        |15,39 L     |
|  <i>Divinópolis ➝ Cláudio</i>        | 55,7 Km                            |0,86 h        |4,09 L      |
|  <i>Divinópolis ➝ Oliveira</i>        | 70,8 Km                            |1,05 h        |5,20 L      |
|  <i>Divinópolis ➝ Formiga</i>        | 80,9 Km                            |1,28 h        |5,94 L      |
|  <i>Divinópolis ➝ Lagoa da Prata</i>        | 96,6 Km                            |1,61 h        |7,10 L      |
|  <i>Divinópolis ➝ Bom Despacho</i>        | 79,6 Km                            |1,21 h        |5,85 L      | 
|  <i>Lagoa da Prata ➝ Bom Despacho</i>        | 52,4 Km                            |1,03 h        |3,85 L      | 
<i>Nova Serrana ➝ Bom Despacho</i>        | 36,7 Km                            |0,61 h        |2,69 L      | 
<i>Cláudio ➝ Oliveira</i>        | 46,1 Km                            |0,75 h        |3,38 L      | 
<center><i>Tabela 1: Informações essenciais para a resolução do trabalho;</i></center><br/>

<p align="justify">⠀⠀⠀⠀Diante do exposto, o leitor agora está apto para ler sobre como tal processo foi implementado, passando passo a passo pelo código desenvolvido, afim de solucionar o problema proposto.</p>

# LÓGICA

<p align="justify">⠀⠀⠀⠀Para que fosse possível inicializar o grafo e começar operar suas configurações iniciais, criou-se o arquivo <i>'node.py'</i>, no qual a classe <code>Node( )</code> é criada e se refere aos vértices que serão utilizados no grafos. Nesta, o construtor da classe do vértice se incia, recebendo os seguintes parâmetros: (<code>self, id, bounty, time_spent</code>). A respeito destes parâmetros, o 'self' funciona como o 'this ➝' do C++; o 'id' representa o número do grafo, no caso, as cidades que serão visitadas; 'bounty' diz respeito a quantia que o engenheiro irá receber ao visitar tal cidade e prestar seu serviço; e 'time_spent' o tempo que será gasto devido ao deslocamento [ Cidade X - Cidade Y ].</p><br/>

<center>
<img src="imgs/EXj1.png" width=450px><br/>
<i>Figura VI: representação de como foi criada a classe referente aos Nós (vértices) do grafo;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Com os vértices inicializados, foi necessário criar agora a classe referente as arestas do grafo. Seguindo o mesmo padrão da classe <code>Node( )</code>, a classe <code>Edge( )</code> também recebe algumas configurações iniciais como parâmetros, são elas: (<code>self, gas_cost, distance, begin, end</code>). Em que cada um, equivale a repectivamente: o mesmo 'this ➝' do C++, o custo da gasolina (por cada litro consumido pelo veículo durante os percursos), a distância a qual o engenheiro terá que dirigir até que chegue em seu cliente e os vértices de partida e chegada, neste caso, a cidade em que ele deixou e a cidade na qual ele pretende chegar. Devido a estas informações carregadas pelas arestas, agora tem-se arestas as quais carregam: seus pesos, nó inicial e nó final, bem como uma variável booleana que tornará possível a movimentação pelo grafo.</p><br/>

<center>
<img src="imgs/EXj2.png" width=450px><br/>
<i>Figura VII: representação de como foi criada a classe referente as Arestas do grafo, bem como foram feitas suas atribuições;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Neste ponto, o grafo já conta com o vértices e arestas capatidos para receberem todas informações necessárias para o funcionamento do programa. Por conta disso, agora será tratado exatamente este ponto: onde e como conseguir tais informações. Bem, o programa foi desenvolvido de tal forma para que os dados fundamentais para a execução do programa fossem coletados a partir de um documento de extensão <code>.txt</code>. O usuário deve inserir todas as informações que aqui já foram citadas em um arquivo que, naturalmente, deve ser nomeado como <code>DADOS.txt</code> (vale ressaltar que este nome pode ser facilmente alterado por outro, bastando apenas alterar a linha < 6 > no <code>main.py</code>. Dentro deste arquivo, é importante que os dados estejam dispostos de uma maneira específica, segue exemplo:</p><br/>

<center>
<img src="imgs/EX3.1.png" width=49%>
<img src="imgs/EXj3.png" width = 50%>
<i>Figuras VII e IX: exemplo de como deve ser configurado o arquivo "DADOS.txt";</i>
</center><br/>
<b>OBS: vide <i>"Figura V"</i> para ficar mais claro a quais cidades os números de identificação equivalem;</b><br/><br/>

<p align="justify">⠀⠀⠀⠀Ainda no arquivo de entrada no qual o usuário tem liberdade para alterar quaisquer configurações que deseja, é necessário a informação sobre os arcos entre os vértices também. Isto é: deve ser informado a distância (em horas, no caso deste trabalho que envolve viagens rodoviárias) entre um vértice e outro (cidades), bem como o gasto médio de combustível para realizar tal viagem. Para tal, foi construída a seguinte estrutura que abrange todos os caminhos possíveis, pelos quais o engenheiro pode passar em algumas de suas viagens:</p><br/>

<center>
<img src="imgs/arcos1.png" width=400px><br/>
<i>Figura X: exemplo de como deve ser escrita as informações sobre os arcos presentes no grafo;</i>
</center><br/>

<p align="justify">⠀⠀⠀⠀Certificando que o arquivo de leitura foi configurado corretamente, pode-se começar a explicar como foi desenvolvido e aplicado o método de leitura do mesmo, assim possibilitando a execução do programa como esperado. Para ler, interpretar e absorver os dados presentes no arquivo de entrada, os subprogramas do arquivo <code>process_file.py</code> foram criados.</p>

<p align="justify">⠀⠀⠀⠀A primeira delas, <code>processfile( )</code> tem um papel simples, porém muito importante para que as demais consigam operar com sucesso: separa todo o arquivo em linhas. Tal ação é realizada utilizando de um loop <i>for</i>, salvando cada linha em uma variável "<code>line</code>" ➝ muito parecido com o formato utilizado para realizar tokenizações em C++. Seguindo com a função <code>processLine( )</code> responsável por "separar" o arquivo, removendo do arquivo, os espaços presentes entre as strings. Dessa forma, já possível criar os vértices, afinal, já estão isolados, fazendo assim a chamada da função <mark>buildEdge( ) *</mark>, que recebe como parâmetro o "pedaço" cortado do arquivo e o grafo como um todo, criando assim, o primeiro e os demais.</p>

<p align="justify">⠀⠀⠀⠀Entrando na função chamada <code>getNumberOfNodes( )</code>, como o nome já sugere, está é responsável por ler todo o grafo (que nessa altura já foi gerado, uma vez que passou antes pela função <code>buildEdge( )</code>) e realiza uma contagem de quantos vértices foram validados neste grafo. A próxima função essêncial para o funcionamento do programa é a chamada <code>getFloatValueFromTitle( )</code>. Pode parecer confuso lendo o nome dado, porém, o que essa função realiza é retorar como um valor flutuante (Float), dado uma string do arquivo, além de remover possíveis '\n', que podem aparecer ao fim das strings lidas. O funcioamento dessa função utiliza do bloco <i>Try Catch</i>, normalmente usado para tratamentos de exceções.</p>

<p align="justify">⠀⠀⠀⠀A função <b><code>buildEdge( ) *</code></b>, citada anteriormente, é responsável por construir uma aresta de acordo com os dados coletados anteriormente pelo arquivo. Com os valores coletados, a função é capaz de ler a distância informada, bem como o consumo médio esperado para tal trajeto. Além disso, a função também adiciona o vértice inicial e o final para a aresta em questão, de forma que, no fim, se tem um vértice com os seguintes atributos:</p>

>edge = Edge{
    ⠀⠀⠀gas_cost,
      ⠀    ⠀  distance,
      ⠀⠀  ⠀begin,
      ⠀⠀  ⠀end
}

<p align="justify">⠀⠀⠀⠀Assim como a função <code>buildEdge( )</code>, que tem como principal objetivo criar as arestas presentes no grafo, a função <code>buildNode( )</code> vem com o propósito praticamente igual. Nesta, o programa constrói um novo vértice, também de acordo com as informações coletadas do arquivo de entrada. Enquanto a outra função ficava responsável por coletar e adicionar a distância e o custo de combustível envolvido, esta agora objetiva alcançar a definição da recompensa sobre o trabalho realizado pelo engenheiro na cidade 'X', bem como definir o tempo no qual tal serviço levará para ser concluido. A função <code>verifyNode( )</code> faz a verificação se algum vértice já consta dentro da estrutura do grafo. Caso seja encontrado, a função retorna <i>true</i>, entretanto, caso o vértice seja novo, ou seja, não foi encontrado dentro do grafo, é relatado um problema ao usuário.</p><br/>

<center>
<img src="imgs/process1.png" width=600px><br/>
<i>Figura XI: função responsável por criar os vértices do grafo a partir dos dados lidos do arquivo de entrada;</i>
</center><br/>


# REFERÊNCIAS
[ I ] https://pt.wikipedia.org/wiki/Teoria_dos_grafos <br/>
[ II ] http://www.mat.ufrgs.br/~portosil/caixeiro.html <br/>
[ III ] https://matplotlib.org/ <br/>
[ IV ] https://numpy.org/ <br/>
[ V ] https://scipy.org/ <br/>
[ VI ] https://networkx.org/ <br/>
[ VII ] https://www.carrosnaweb.com.br/fichadetalhe.asp?codigo=2274 
hamilton https://www.inf.ufsc.br/grafos/temas/hamiltoniano/hamiltoniano.htm
<br/>