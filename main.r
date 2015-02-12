setwd('/Users/isaiah/Dropbox/programming/kaggle/rain')
rain.data = read.table("processed_train_2013.csv",header=T)
attach(rain.data)
#labels
	#Id,TimeToEnd,DistanceToRadar,Composite,HybridScan,HydrometeorType,Kdp,RR1,RR2,RR3,RadarQualityIndex,Reflectivity,ReflectivityQC,RhoHV,Velocity,Zdr,LogWaterVolume,MassWeightedMean,MassWeightedSD,Expected


#full model
fit=lm(Expected~TimeToEnd+DistanceToRadar+Composite+HybridScan+HydrometeorType+Kdp+RR1+RR2+RR3+RadarQualityIndex+Reflectivity+ReflectivityQC+RhoHV+Velocity+Zdr+LogWaterVolume+MassWeightedMean+MassWeightedSD)
summary(fit)
#quantile(fit$residuals , prob=c(0.025, 0.5, 0.975))
#BIC(fit)
#vif(fit) 

'''
#ground
fit2=lm(quan_ew~max_g+min_g+ind_g)
summary(fit)
BIC(fit) 

#air
fit3=lm(quan_ew~max_g)
summary(fit)$adj.r.squared
summary(fit)
BIC(fit) 

par(mfrow=c(2, 2))
plot(fitted(fit),residuals(fit),ylab="raw residuals",xlab="fitted values", main = "raw residuals vs. fitted values") 
abline(h=0)

#studentized residuals
plot(fitted(fit),rstudent(fit),xlab="fitted values",ylab="studentized residuals", main = "studentized residuals vs. fitted values")
abline(h=0)

qqnorm(rstudent(fit),xlab="standard normal quantiles",ylab="studentized residuals quantiles", main = "QQ plot to ascces normality of residuals")

cook = cooks.distance(fit)
plot(1:length(cook),cook, main = "cooks distance for values")
'''