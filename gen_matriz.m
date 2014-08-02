function [ M ] = gen_matriz(n)
    a=[1 -1 ; -1 1];
    M=n*a;
    for i=1:n
        j=1;
        M(i:i+j,i:i+j)=a;
    end
    
    
    
    for i=1:n+1
        for j=1:n+1
            if i==j
                if i~=1
                    if i~=n+1
                        M(i,j)=2;
                    end
                end
            end
        end
    end
    
    
end
