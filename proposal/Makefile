filename=proposal

mpc: 
		pdflatex --shell-escape ${filename}.tex
		evince ${filename}.pdf &
		rm -rf ${filename}.log ${filename}.aux missfont.log _minted-${filename} texput.log
