function z = newton(prob,ini)
% ニュートン法
% probは問題番号、iniは初期値を示す
	x=ini;
	iter = 1
	delta=10
	if prob == 1
		% 更新の量deltaが0.0001より小さくなるまで計算する
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
		% 更新の量deltaが0.0001より小さくなるまで計算する
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
% 式1の関数
	y1=1/x+exp(x);
endfunction

function y2 = diff_prob1(x)
% 式1の導関数
	y2 = -1/x**2+exp(x);
endfunction

function dd1 = diff2_prob1(x)
% 式1の2次導関数
	dd1 = 2/x**3+exp(x);
endfunction

function y3 = prob2(x)
% 式2の関数
	y3=sin(5*x)+(x-5)**2;
endfunction

function y4 = diff_prob2(x)
% 式2の導関数
	y4 = 5*cos(5*x) + 2*(x-5);
endfunction

function dd2 = diff2_prob2(x)
% 式2の２次導関数
	dd2 = -25*sin(5*x) + 2;
endfunction
