filename=report

pdf: 
		pdflatex --shell-escape ${filename}.tex

read:
		evince ${filename}.pdf &


clean:
		rm -rf ${filename}.log ${filename}.aux missfont.log _minted-${filename} texput.log *.bbl *.blg *.lof *.toc *.out

wc:
		echo 'WORD COUNT: '
		pdftotext ${filename}.pdf - | tr -d '.' | wc -w

mpc:
		pdflatex --shell-escape ${filename}.tex

		#FOR LINUX:
	    #evince ${filename}.pdf &
		#FOR OS X:
	    open ${filename}.pdf &
        
		rm -rf ${filename}.log ${filename}.aux missfont.log _minted-${filename} texput.log *.bbl *.blg *.lof *.toc *.out

		echo 'WORD COUNT: '
		#FOR LINUX:
		pdftotext ${filename}.pdf - | tr -d '.' | wc -w
		#FOR OS X:
        #ps2ascii myfile.pdf | wc -w
