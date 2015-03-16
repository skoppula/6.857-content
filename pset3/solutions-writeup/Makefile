file=solutions
finalname=pset3
author1=julia_h
author2=toyk2a
author3=skoppula

pdf: 
		pdflatex --shell-escape ${file}.tex

read:
		evince ${file}.pdf &

split:
		gs -sDEVICE=pdfwrite -dSAFER -o ${author1}_${author2}_${author3}_${finalname}_problem%d.pdf ${file}.pdf

clean:
		rm -rf ${file}.log ${file}.aux missfont.log _minted-${file} texput.log

