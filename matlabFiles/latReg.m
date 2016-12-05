function [res] = latReg( featureNum )

load('bussinessPlusTopics.mat')
latentFeatures = csvread('/Users/Nick/Documents/Fall 2016/Big Data/abby/correctLatentFeatures.csv');
rawFeature = latentFeatures(:,featureNum); %5 ~10
feature = [];
rData = [];

%Get the data points which actually has the features
for i = 1:length(rawFeature)
    if rawFeature(i) > -.5
        feature = [feature ; rawFeature(i)];
        rData = [rData ; W(i,:)];
    end  
end

numPoints = length(feature);

feaTrain = feature(1:2*numPoints/3);
rDataTrain = rData(1:2*numPoints/3,:);

feaTest = feature(2*numPoints/3 : numPoints);
rDataTest = rData(2*numPoints/3 : numPoints,:);

b = regress(feaTrain, rDataTrain);

rawPred = rDataTest * b;

pred = [];

for i = 1:length(feaTest)
    if rawPred(i) < 0.5
        pred = [pred; 0];
    else
        pred = [pred; 1];
    end
end

results = pred - feaTest;

SampleNum = length(feaTest);

NumPos = length(feaTest(feaTest==1));

NumNeg = length(feaTest(feaTest==0));

FP = length(results(results==1)) / NumNeg;

FN = length(results(results==-1)) / NumPos;

Accuracy = (SampleNum - sum(abs(results)))/ SampleNum;

res = [Accuracy,  NumPos, NumNeg, FP, FN ];


end

