file=solutions
finalname=pset2
author1=chenp
author2=cpp0101
author3=skoppula

pdf: 
		pdflatex --shell-escape ${file}.tex

read:
		evince ${file}.pdf &

split:
		gs -sDEVICE=pdfwrite -dSAFER -o ${author1}_${author2}_${author3}_${finalname}_problem%d.pdf ${file}.pdf

clean:
		rm -rf ${file}.log ${file}.aux missfont.log _minted-${file} texput.log

