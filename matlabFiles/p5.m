%fea and reuters were importaned from an online dataset at
%http://www.cad.zju.edu.cn/home/dengcai/Data/TextData.html
[W,H,obj] = nmf(fea, 20);
plot(obj);
hold on
title('Convergence of nmf')
xlabel('Iteration')
ylabel('Objective Function')
hold off

[val, idx] = sort(H','descend');
topics = idx(1:20,:);

res = cell(21,20);
for i = 1:20
    res{1,i} = strcat('Topic  ', num2str(i));
end
    

for i = 1:20
    res(2:21,i) = Terms(topics(:,i));
end
    
