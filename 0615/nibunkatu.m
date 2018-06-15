function z = nibunkatu(prob)
% 二分割法
% probは問題番号
	a = 0
	b = 10
	iter = 1
	if prob == 1
	% 区間[a,b]が0.0001より小さくなるまで計算する
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
	% 区間[a,b]が0.0001より小さくなるまで計算する
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
% 式1の関数
	y1=1/x+exp(x);
endfunction

function y2 = diff_prob1(x)
% 式1の導関数
	y2 = -1/x**2+exp(x);
endfunction

function y3 = prob2(x)
% 式2の関数
	y3=sin(5*x)+(x-5)**2;
endfunction

function y4 = diff_prob2(x)
% 式2の導関数
	y4 = 5*cos(5*x) + 2*(x-5);
endfunction
