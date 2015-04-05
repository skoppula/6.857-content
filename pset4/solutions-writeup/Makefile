file=solutions
finalname=pset4
author1=m_chang
author2=nbravo
author3=skoppula

pdf: 
		pdflatex --shell-escape ${file}.tex

read:
		evince ${file}.pdf &

split:
		gs -sDEVICE=pdfwrite -dSAFER -o ${author1}_${author2}_${author3}_${finalname}_problem%d.pdf ${file}.pdf

clean:
		rm -rf ${file}.log ${file}.aux missfont.log _minted-${file} texput.log

mpc:
		pdflatex --shell-escape ${file}.tex
		evince ${file}.pdf &
		rm -rf ${file}.log ${file}.aux missfont.log _minted-${file} texput.log


