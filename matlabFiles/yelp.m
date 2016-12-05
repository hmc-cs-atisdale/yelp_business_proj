freq = csvread('/Users/Nick/Documents/Fall 2016/Big Data/abby/reveiwFreq.csv');
% 
fid = fopen('/Users/Nick/Documents/Fall 2016/Big Data/abby/reveiwWordList.csv','r');
C = textscan(fid, repmat('%s',1,10), 'delimiter',';', 'CollectOutput',true);
C = C{1}{1};
words = strsplit(C,',');
fclose(fid);
% 
sFreq = sparse(freq);
k = 20;
[W,H] = nnmf(sFreq,20);
% [W,H,obj] = nmf(sFreq, 20);
% plot(obj);
% hold on
% title('Convergence of nmf')
% xlabel('Iteration')
% ylabel('Objective Function')
% hold off

[val, idx] = sort(H','descend');
lenTopics = 30;
topics = idx(1:lenTopics,:);

res = cell(lenTopics+1,k);
for i = 1:k
    res{1,i} = strcat('Topic  ', num2str(i));
end
    

for i = 1:k
    res(2:lenTopics + 1,i) = words(topics(:,i));
end