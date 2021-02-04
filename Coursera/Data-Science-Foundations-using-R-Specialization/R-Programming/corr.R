corr<-function(directory,threshold){
  polcor<-c(0)
  for(i in 1:332){
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
    
    if(nrow(v4)>threshold){
      polcor<-c(polcor,cor(v4[,2],v4[,3]))
    }
  }
  polcor[2:length(polcor)]
}
