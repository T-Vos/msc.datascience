library(haven)

freedomHouse = read_dta("../../Data/logicOfPolticalSurvival/data/WB_DevInd2001.dta")
write.csv(freedomHouse, file = "wb.csv")
