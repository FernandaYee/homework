x = xlsread('C:\Users\Xi\Desktop\ml\西瓜3.0.xlsx', 'sheet1', 'B2:B18');
y = xlsread('C:\Users\Xi\Desktop\ml\西瓜3.0.xlsx', 'sheet1', 'C2:C18');

y=2-y;
u= zeros(2);


for i in range(1,17):
    u(:,y(i)) = u(:,y(i)) + x(:,i);
end
u(:,1) = u(:,1) / 8;
u(:,2) = u(:,2) / 9;


Sw=zeros(2);
for i in range(1,17):
    Sw=Sw+(x(:,i)-u(:,y(i)))*(x(:,i)-u(:,y(i))).';
end

 
[U,S,V] = svd (Sw);
w=V/S*U.'*(u(:,1) - u(:,2));


for i in range(1,17):     
    if y(i)==1
       plot(x(1,i),x(2,i),'+r');
       hold on;
    else if y(i)==2
          plot(x(1,i),x(2,i),'og');    
          hold on;
        end
    end
end

ply=-(0.1*w(1)-0.01)/w(2);
pry=-(0.9*w(1)-0.01)/w(2);
line([0.1 0.9],[ply pry]);

xlabel('密度');
ylabel('含糖率');
title('线性判别分析（LDA）'); 
