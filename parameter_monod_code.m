umax = 0.43;
Ks = 1.2;
Yx_s = 1.21;

real_data_time = [0 4 8 12 16 20 24 28];
real_data_od = [0.15 0.37 0.79 1.2 1.46 1.53 1.59 1.6];

%time interval and initial conditions
t_interval = [0 28];
init_cond = [0.15 1.2];

f = @(t,x)[x(1)*umax*x(2)/(Ks+x(2));-(x(1)*umax*x(2)/(Yx_s*(Ks+x(2))))];



%solution
[t,x] = ode45(f, t_interval , init_cond);
%plot
plot(t,x(:,1),'b',t,x(:,2),'r');
hold on
scatter(real_data_time(:),real_data_od(:),'k')
legend('X','S')
title('X and S vs Time')
ylabel('X (od600), S (g)'),xlabel('Time (hrs)')
