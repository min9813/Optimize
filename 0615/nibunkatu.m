function z = nibunkatu(prob)
	a = 0
	b = 10
	iter = 1
	if prob == 1
		while(abs(b-a)>0.0001)
			l=(a+b)/2;
			df=diff_prob1(l);
			if df>0
				b = l;
			else
				a = l;
			endif
			iter
			b-a
			++iter;
		endwhile
		a
		z = prob1(a)
	else
		while(abs(b-a)>0.0001)
			l=(a+b)/2;
			df=diff_prob2(l);
			if df>0
				b = l;
			else
				a = l;
			endif
			iter
			b-a
			++iter;
		endwhile
		a
		z = prob2(a)
	endif
endfunction



function y1 = prob1(x)
	y1=1/x+exp(x);
endfunction

function y2 = diff_prob1(x)
	y2 = -1/x**2+exp(x);
endfunction

function y3 = prob2(x)
	y3=sin(5*x)+(x-5)**2;
endfunction

function y4 = diff_prob2(x)
	y4 = 5*cos(5*x) + 2*(x-5);
endfunction




	