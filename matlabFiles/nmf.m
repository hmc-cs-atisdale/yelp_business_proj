function [ W, H, obj ] = nmf( X, k )
%UNTITLED2 Non-Negitive matrix factorization, an explination of the
%algorithm can be found at: 
%https://papers.nips.cc/paper/1861-algorithms-for-non-negative-matrix-factorization.pdf

%Define some system parameters
printFreq = 5;
numIter = 100;

sizeX = size(X);
W = abs(randn(sizeX(1),k)*1e-3);
H = abs(randn(k,sizeX(2))*1e-3);

diff = X - W*H;


%Claculate the Frobenius norm which is equivalent to the squared ecludiean
obj = zeros(numIter,1);
obj(1) = sum(sum(diff.^2,1),2);%norm(diff, 'fro');

obj(1)


for i = 1:numIter
    if mod(i,printFreq) == 0
        i-1
        obj(i-1)
    end
    
    H = H .* (W'*X) ./ ((W'*W)*H);
    W = W .* (X*H') ./ (W*(H*H'));

    diff = X - W*H;
    %Claculate the Frobenius norm which is equivalent to the squared ecludiean
    obj(i) = sum(sum(diff.^2,1),2);%norm(diff, 'fro');
end

    

end

