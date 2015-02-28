file=solutions

pdf: 
		pdflatex --shell-escape ${file}.tex

read:
		evince ${file}.pdf &

clean:
		rm -rf ${file}.log ${file}.aux missfont.log _minted-${file} texput.log

