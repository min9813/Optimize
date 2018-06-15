function z = newton(prob,ini)
	x=ini;
	iter = 1
	delta=10
	if prob == 1
		while(abs(delta)>0.0001)
			delta = -diff_prob1(x)/diff2_prob1(x);
			x = x + delta;
			iter
			delta
			x
			printf("---------------");
			++iter;
		endwhile
		x
		z = prob1(x)
	else
		while(abs(delta)>0.0001)
			delta = -diff_prob2(x)/diff2_prob2(x);
			x = x+ delta;
			iter
			delta
			x
			printf("---------------");
			++iter;
		endwhile
		x
		z = prob2(x)
	endif
endfunction



function y1 = prob1(x)
	y1=1/x+exp(x);
endfunction

function y2 = diff_prob1(x)
	y2 = -1/x**2+exp(x);
endfunction

function dd1 = diff2_prob1(x)
	dd1 = 2/x**3+exp(x);
endfunction

function y3 = prob2(x)
	y3=sin(5*x)+(x-5)**2;
endfunction

function y4 = diff_prob2(x)
	y4 = 5*cos(5*x) + 2*(x-5);
endfunction

function dd2 = diff2_prob2(x)
	dd2 = -25*sin(5*x) + 2;
endfunction



	