filename1=ericadu_skoppula_jzwang_pset1_problem1
filename2=ericadu_skoppula_jzwang_pset1_problem2
filename3=ericadu_skoppula_jzwang_pset1_problem3

pdf: 
		pdflatex --shell-escape ${filename1}.tex
		pdflatex --shell-escape ${filename2}.tex
		pdflatex --shell-escape ${filename3}.tex

read:
		evince ${filename1}.pdf &
		evince ${filename2}.pdf &
		evince ${filename3}.pdf &

clean:
		rm -rf ${filename1}.log ${filename1}.aux missfont.log _minted-${filename1} texput.log
		rm -rf ${filename2}.log ${filename2}.aux missfont.log _minted-${filename2} texput.log
		rm -rf ${filename3}.log ${filename3}.aux missfont.log _minted-${filename3} texput.log

