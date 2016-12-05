results = [];
for i = 1:23
    %[Accuracy,  NumPos, NumNeg, FP, FN ] = latReg(i);
    results = [results ; latReg(i)];
end

metrics = {'Accuracy', 'Number of Positive', ...
    'Number of Negitive', 'False Positives', 'False Negitive' }; 

headers = {'Takes Reservations'	'Take-out'	'Delivery'	'Has TV' ...
    'Waiter Service'	'Good for Kids'	'Outdoor' 'Seating' ...
    'Good For Groups'	'Drive-Thru'	'Accepts Credit Cards'	'Caters'...
    'Happy Hour'	'Good For Dancing'	'Coat Check'	'Wheelchair Accessible' ...
    'Dogs Allowed'	'Corkage'	'Order at Counter'	'BYOB'	'By Appointment Only' ...
    'Accepts Insurance'	'Open 24 Hours'};
clf
% for i = 1:5
%     figure(i);
%     bar(results(:,i));
%     title(metrics(i))
% end
results = [results(1:5,:); results(7:23 ,:)];
figure(1);
bar(results(:,1));
title('Accuracy for Prediciting Various Latent Features');
set(gca,'XTick',1:22)
set(gca,'XTickLabel',headers)
set(gca,'XTickLabelRotation',45)

figure(2);
subplot(2,1,1);
hb = bar(results(:,4:5));
title('Precent of False Positives and Negitives for Predicting Latent Features');
set(gca,'XTick',1:22)
set(gca,'XTickLabel',headers)
set(gca,'XTickLabelRotation',45)


subplot(2,1,2);
hb = bar(results(:,2:3));
title('Number of Positive and Negitive Data Points in Training Set ');
set(gca,'XTick',1:22)
set(gca,'XTickLabel',headers)
set(gca,'XTickLabelRotation',45)

hbc = get(hb, 'Children');
set(hbc{1}, 'FaceColor', 'r');
set(hbc{2}, 'FaceColor', 'g');
legend('Positive','Negitive');

