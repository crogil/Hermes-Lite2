

import BOM

optionset = set(['NOSWCLK','REGPA','PA','LVDS25','ETH25','ETH','VERSA','VBIAS','VOP',
	'RXLPF','RXNPOL','TXLPF','TXPREAMP','TXSW','TXLP','LED','FRONTIO','ADC','THERMAL',
	'PATR','EXTPTT','EXTFILTER','VERSAOSC','CASE','PROGRAMMER'])

## 'NOASSEMBLY' to include parts needed by not put on by assembly house

bom = BOM.BOM("../hermeslite.xml",optionset=optionset)


bom.CSVAssemblyPrint(['Mouser','Digi-Key'])


