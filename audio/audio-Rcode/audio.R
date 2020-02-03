  library(warbleR)
  global1 <- data.frame(matrix(ncol = 25, nrow = 0))
  colnames(global1)=c("class","sound.files","selec","duration","meanfreq","sd","median","Q25","Q75",
  "IQR","skew","kurt","sp.ent","sfm","mode",
  "centroid","peakf","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx")
  
  ##########################################################################################
  
  setwd("/home/lawrence/udemy/audio/Audio/Hello/")
  
  for (i in 32:48){
  	print(i)
  	track  = paste("Track",i,sep="")
  	track  = paste(track,".wav",sep="")
  	print(getwd())
  	X = data.frame(sound.files=track,selec=0,start=0,end=1, bottom.freq=0, top.freq=44000)
  	a <- specan(X)
  	a["class"] = "Hello"
  	print(a)
  	global1 = rbind(global1,a)
  }

##########################################################################################

setwd("/home/lawrence/udemy/audio/Audio/Goodbye")

for (i in 54:66){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1, bottom.freq=0, top.freq=44000)
	a <- specan(X)
	a["class"] = "Goodbye"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("/home/lawrence/udemy/audio/Audio/Banana")

for (i in 70:87){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1, bottom.freq=0, top.freq=44000)
	a <- specan(X)
	a["class"] = "Banana"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("/home/lawrence/udemy/audio/Audio/Chair")

for (i in 106:118){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1, bottom.freq=0, top.freq=44000)
	a <- specan(X)
	a["class"] = "Chair"
	print(a)
	global1 = rbind(global1,a)
}

##########################################################################################

setwd("/home/lawrence/udemy/audio/Audio/IceCream")

for (i in 89:101){
	print(i)
	track  = paste("Track",i,sep="")
	track  = paste(track,".wav",sep="")
	X = data.frame(sound.files=track,selec=0,start=0,end=1, bottom.freq=0, top.freq=44000)
	a <- specan(X)
	a["class"] = "IceCream"
	print(a)
	global1 = rbind(global1,a)
}

########################################################################################## 



global2 = na.omit(global1)

write.csv(global2,"/home/lawrence/udemy/audio/Audio/data_model.csv")


##########################################################################################
##########################################################################################

validation <- data.frame(matrix(ncol = 25, nrow = 0))
colnames(validation )=c("class","sound.files","selec","duration","meanfreq","sd","median","Q25","Q75",
"IQR","skew","kurt","sp.ent","sfm","mode",
"centroid","peakf","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx")

setwd("/home/lawrence/udemy/audio/Audio/validation")
path="/home/lawrence/udemy/audio/Audio/validation"

file.names <- dir(path, pattern =".wav")
for(i in 1:length(file.names)){
  filename = unlist(strsplit(file.names[i],"_"))[1]
  X = data.frame(sound.files=file.names[i],selec=0,start=0,end=1, bottom.freq=0, top.freq=44000)
  a <- specan(X)
  a["class"] = filename
  validation = rbind(validation ,a)
}
	
###########################################################################################

validation = na.omit(validation)

write.csv(validation ,"/home/lawrence/udemy/audio/Audio/validation.csv")  