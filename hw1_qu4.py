X=[];
Y=[];
Z=[];
counter=1;
for x=3:2:15
for y=17:5:100
A=imread('http://cs.brown.edu/courses/csci1430/proj1a/RISDance.jpg');
scale=y/100;
resized_A=imresize(A,scale);
kernel = fspecial('gaussian',x,x);
tic;
filtered_A = imfilter(resized_A,kernel);
time=toc;
X(counter)=x;
Y(counter)=y;
Z(counter)=time;
counter=counter+1;
end;
end;
A=vertcat(X,X,X,X,X,X,X,X,X,X);
B=vertcat(Y,Y,Y,Y,Y,Y,Y,Y,Y,Y);
C=vertcat(Z,Z,Z,Z,Z,Z,Z,Z,Z,Z);
surf(A,B,C)