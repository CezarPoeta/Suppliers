//=======================Variáveis Controlam Movimento no Grid=====================================
var tlg            =  15;   //TOTAL DE Rows NO GRID 
var pat            =   0;   //POSIÇÃO ATUAL - AZUL NO AMARELO
var pan            =   0;   //POSIÇÃO ANTERIOR - PRETO NO BRANCO
var ctrIniPag      =   0;   //CONTROLA INÍCIO DE APRESENTAÇÃO NO GRID
var ctrFimPag      = tlg;   //CONTROLA FINAL DE APRESENTAÇÃO NO GRID
var tll            =   0;   //TLL - TOTAL DE REGISTROS LIDOS
var ctrUltimaLinha =   0;   //CONTROLA ÚLTIMA LINHA DO GRID

//=======================Variáveis controlam Evento nos botões=====================================
//var button_new        = document.querySelector("#idNovo");
//var button_save       = document.querySelector("#idSalvar");
//var button_delete     = document.querySelector("#idExcluir");
//var button_search     = document.querySelector("#idBuscar");
//var quadroDeVariaveis = document.querySelector("#Grafico1");

//=======================Variáveis privadas da Classe==============================================
var tableBody  = document.querySelector("tbody");                 //Onde as Rows serão incluidas
var myTable    = document.querySelector("table#tabela");          //Possibilita editar registro da myTable
var field_id   = document.querySelector("input[name='iId']");     //Dado lido do formulário
var field_name = document.querySelector("input[name='sNome']");   //Dado lido do formulário

//=======================Controle Setas Cima/Baixo=================================================
document.addEventListener("keydown", function (event) {
    var obj = document.getElementById("tbody");
    var tecla = event.keyCode;

    if (tecla == 38){
        subtraiPat();
    };

    if (tecla == 40){
        somaPat();
    };
});
//----------------------Controle Leitura do BD e Apresentação dos dados na Tabela ----------------- 
function somaPat() {
    pat++;
    if (tll > tlg) {        // Total Registros > Total Linhas Grid
        if (pat > tlg){     // Se posição Atual for Maior que Total de linhas no grid
            ctrIniPag++;
            ctrFimPag++;           
            ctrUltimaLinha = ctrFimPag + 1; //Controla paginação

            if(ctrUltimaLinha > tll){
                window.alert("Último Registro!")
                ctrIniPag--;
                ctrFimPag = tll;
                ctrUltimaLinha = tll;
            }
            pat = tlg;
            pan = 0;
            loadData();
        }else {
            selectRow(pan,pat);                
            pan = pat;
        }
    } else {  // Total Registros < Total Linhas Grid
        if (pat >= tlg){   //Se posição Atual for Maior que Total de linhas no grid
            window.alert("FOI ESTE - Último Registro!")
            pat--;
            selectRow(pan,pat);
            pan = pat;
        }else {
            selectRow(pan,pat);
            pan = pat;
        }

    }
}

function subtraiPat() {
    pat--;
    if (tll - pat != 0){console.log(ctrIniPag)}
    if (pat < 0){     //Se posição Atual for menor que zero
        ctrIniPag--;
        ctrFimPag--;

        if(ctrIniPag < 0){
            window.alert("Primeiro Registro!")
            ctrIniPag = 0;
            ctrFimPag = tlg;
        }
        pat = 0;
        pan = 0;
        loadData();
    } else{
        selectRow(pan,pat);                
        pan = pat;    
    }
}

//=======================Controle Seleção da Linha=================================================
function selectRow(ppan, ppat) {
    //Altera a cor da TR Anterior para cor original
    tableBody.rows[ppan].style.background = 'white';  
    tableBody.rows[ppan].style.color = 'black';
    tableBody.rows[ppan].style.fontWeight = 'normal';

    //Altera a cor da TR Atual para cor azul / amarelo
    tableBody.rows[ppat].style.background = 'yellow';  
    tableBody.rows[ppat].style.color = 'blue';
    tableBody.rows[ppat].style.fontWeight = 'bold';

    //Mostra dados no Form
    //document.querySelector("input[name='iId']").value = myTable.rows[ppat + 1].cells[0].innerHTML;
    //document.querySelector("input[name='sNome']").value = myTable.rows[ppat + 1].cells[1].innerHTML;
}


function loadData() {
    // Limpa a tableBody para atualização
//    var iFim = tableBody.rows.length;
//    for (var i = 0; i < iFim;i++) {
//        tableBody.deleteRow("0");
//    }
    // Inclui Rows na tableBody   
//    db.transaction(function (pSQL) {
//        pSQL.executeSql('SELECT id, nome FROM tblBeneficiarios', [],function (pSQL,resultado) {
 //           var rows = resultado.rows;
  //          tll = rows.length;
  //          for (var i = 0; i < rows.length;i++) {
  //              var template = document.querySelector("#template1");
   //             lista_td = template.content.querySelectorAll("td");
   //             lista_td[0].textContent = rows[i].id;
   //             lista_td[1].textContent = rows[i].nome;
   //             var novaTR = document.importNode(template.content, true);
   //             if (i>=ctrIniPag && i<=ctrFimPag){
   //                 tableBody.appendChild(novaTR);
   //             }
    //        }
            selectRow(pan, pat);
            pan = pat;
    //    })
//    })
}
