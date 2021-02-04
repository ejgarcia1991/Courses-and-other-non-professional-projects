complete<-function(directory,id=1:332){
  data<-data.frame("0",0)
  names(data)[1]<-"id"
  names(data)[2]<-"nobs"
  for(i in id){
    dir<-i
    if(i<10){
      dir<-paste("0",dir,sep="")
    }
    if(i<100){
      dir<-paste("0",dir,sep="")
    }
    var<-read.csv(paste(directory,"\\",dir,".csv",sep=""))
    var<-as.data.frame(var)
    v<-var[!is.na(var)[,1],]
    v2<-v[!is.na(v)[,2],]
    v3<-v2[!is.na(v2)[,3],]
    v4<-v3[!is.na(v3)[,4],]
    
    n<-data.frame(dir,nrow(v4))
    names(n)[1]<-"id"
    names(n)[2]<-"nobs"
    
    data<-rbind(data,n)
  }
  data[2:nrow(data),]
}
