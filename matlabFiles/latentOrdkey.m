load('bussinessPlusTopics.mat')
ratings = csvread('/Users/Nick/Documents/Fall 2016/Big Data/abby/ratingsRevised.csv');
rawFeature = ratings; %5 ~10
feature = [];
rData = [];

%Get the data points which actually has the features
for i = 1:length(rawFeature)
    if rawFeature(i) > -.5
        if rawFeature(i) < 3
            revisedCat = 1;
        elseif  rawFeature(i) < 4
            revisedCat = 2;
        else 
            revisedCat = 3;
        end
        feature = [feature ; revisedCat];
        rData = [rData ; W(i,:)];
    end
        
        
        
end

numPoints = length(feature);

feaTrain = feature(1:2*numPoints/3);
rDataTrain = rData(1:2*numPoints/3,:);

feaTest = feature(2*numPoints/3 : numPoints);
rDataTest = rData(2*numPoints/3 : numPoints,:);

b = mnrfit(rDataTrain,feaTrain);

[y,I] =  sort(mnrval(b,rDataTest),2,'descend');


pred = I(:,1);


results = pred - feaTest;

SampleNum = length(feaTest);

NumOne = length(feaTest(feaTest==1))

NumTwo = length(feaTest(feaTest==2))

NumThree = length(feaTest(feaTest==3))

Accuracy = length(results(results==0))/ SampleNum

