filename=pset1

pdf: 
		pdflatex --shell-escape ${filename}.tex

read:
		evince ${filename}.pdf &

clean:
		rm -rf ${filename}.log ${filename}.aux missfont.log _minted-${filename} texput.log

