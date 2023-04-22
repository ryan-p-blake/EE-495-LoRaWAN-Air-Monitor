% 
% fileID = fopen('tmp.txt','r');
% formatSpec = '%f';
% 
% A = fscanf(fileID,formatSpec);
% 
% plot(A)
% title("Tempurature Data Over Time")
% xlabel("Time in 10s Intervals")
% ylabel("Tempurature Deg C")
% 
% 
% fclose(fileID);

% specify the node number you want to view data for
selected_node = 1;

% open the files for reading
pm2_5_file = fopen(fullfile('DataFolder', sprintf('pm2.5_%d.txt', selected_node)), 'r');
pm4_0_file = fopen(fullfile('DataFolder', sprintf('pm4.0_%d.txt', selected_node)), 'r');
pm10_file = fopen(fullfile('DataFolder', sprintf('pm10_%d.txt', selected_node)), 'r');
humidity_file = fopen(fullfile('DataFolder', sprintf('humidity_%d.txt', selected_node)), 'r');
tmp_file = fopen(fullfile('DataFolder', sprintf('tmp_%d.txt', selected_node)), 'r');
voc_file = fopen(fullfile('DataFolder', sprintf('voc_%d.txt', selected_node)), 'r');

if(selected_node == 0)
    pm2_5_file = fopen(fullfile('DataFolder', sprintf('pm2.5_0.0.txt', selected_node)), 'r');
    pm4_0_file = fopen(fullfile('DataFolder', sprintf('pm4.0_0.0.txt', selected_node)), 'r');
    pm10_file = fopen(fullfile('DataFolder', sprintf('pm10_0.0.txt', selected_node)), 'r');
    humidity_file = fopen(fullfile('DataFolder', sprintf('humidity_0.0.txt', selected_node)), 'r');
    tmp_file = fopen(fullfile('DataFolder', sprintf('tmp_0.0.txt', selected_node)), 'r');
    voc_file = fopen(fullfile('DataFolder', sprintf('voc_0.0.txt', selected_node)), 'r');
end

    
% read in all the data from the files
formatSpec = '%f';
pm2_5_data = fscanf(pm2_5_file, formatSpec);
pm4_0_data = fscanf(pm4_0_file, formatSpec);
pm10_data = fscanf(pm10_file, formatSpec);
humidity_data = fscanf(humidity_file, formatSpec);
tmp_data = fscanf(tmp_file, formatSpec);
voc_data = fscanf(voc_file, formatSpec);

% close the files
fclose(pm2_5_file);
fclose(pm4_0_file);
fclose(pm10_file);
fclose(humidity_file);
fclose(tmp_file);
fclose(voc_file);

% create a figure with subplots for each variable
figure;
% set the y-axis limits for each variable based on typical values
pm2_5_ylim = [0, max(pm2_5_data) * 1.5];
pm4_0_ylim = [0, max(pm4_0_data) * 1.5];
pm10_ylim = [0, max(pm10_data) * 1.5];
humidity_ylim = [0, 100];
tmp_ylim = [0, 120];
voc_ylim = [0, max(voc_data) * 1.5];

subplot(3, 2, 1);
plot(pm2_5_data);
title(sprintf('PM2.5 Data for Node %d', selected_node));
xlabel('Time (60s Intervals)');
ylabel('PM2.5 (ug/m^3)');
ylim(pm2_5_ylim);

subplot(3, 2, 2);
plot(pm4_0_data);
title(sprintf('PM4.0 Data for Node %d', selected_node));
xlabel('Time (60s Intervals)');
ylabel('PM4.0 (ug/m^3)');
ylim(pm4_0_ylim);

subplot(3, 2, 3);
plot(pm10_data);
title(sprintf('PM10 Data for Node %d', selected_node));
xlabel('Time (60s Intervals)');
ylabel('PM10 (ug/m^3)');
ylim(pm10_ylim);

subplot(3, 2, 4);
plot(humidity_data);
title(sprintf('Humidity Data for Node %d', selected_node));
xlabel('Time (60s Intervals)');
ylabel('Humidity (%)');
ylim(humidity_ylim);

subplot(3, 2, 5);
plot(tmp_data);
title(sprintf('Temperature Data for Node %d', selected_node));
xlabel('Time (60s Intervals)');
ylabel('Temperature (F)');
ylim(tmp_ylim);

subplot(3, 2, 6);
plot(voc_data);
title(sprintf('VOC Data for Node %d', selected_node));
xlabel('Time (60s Intervals)');
ylabel('VOC (ppb)');
ylim(voc_ylim);
