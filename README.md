# Proposal for the Final Project
## Title: Deforestation rates in the Amazon forest through satellite images
 
 This is a proposal for the final project, for the Image Enhancement discipline, addressing the deforestation of the Amazon rainforest as a theme.
 
 **Student:**
 
 - Normando de Campos Amazonas Filho, NUSP: 11561949
 - Robson Pessoa, NUSP: 8632563
 
 **Title: Deforestation rates in the Amazon forest through satellite images**

Abstract: This project aims to identify and quantify the deforestation of the Amazon rainforest using as an example 2 comparative images (2000 and 2017) from a NASA LANDSAT satellite, where each pixel represents an area of 0.09 ha or 900m². This type of quantification where pixels are related to measurements is known as photogrammetry. The project has 3 important phases: the first is pre-processing where the aim is to improve the image (eliminating noise through filters). The second phase is to define regions of interest and extract them (segmentation). Finally, the third phase consists of generating a statistic comparing the established metrics.

**Main objective**

 This project seeks to understand the methodology adopted by INPE in calculating the rate of deforestation in the Amazon, in the so-called PRODES program (Program for Calculating Deforestation in the Amazon). This methodology was originally developed by the INPE team during the period 1988-2002 to be used in the context of the PRODES Analógico project. In this period, the interpretation of the images was done by visual interpretation of images printed on photographic paper.
Since 2003, INPE has adopted the computer-assisted interpretation process for calculating the deforestation rate in the Amazon, called the PRODES Digital program to distinguish it from the previous process.
 It should be noted that the procedures used by INPE in the period 1988-2002 were never properly documented by those responsible at the time. The 2006 methodology document is the first available description of the fee calculation procedures. It is also worth remembering that INPE started to publish digital maps that describe deforestation in the Amazon only as of 2003. Until then, this information was restricted and not accessible even to other government agencies, which had serious consequences, as it reduced a lot the capacity of the government and society to combat deforestation.
The project will try to understand which are the applied methods that allow an identification and quantification of regions that are extremely vast and difficult to access. 

**Description of Input Images**

 In this project are going to be used two comparative 30 – meter images, of the year 2000 and 2017, obtained from a NASA LANDSAT satellite, that have a dimension of 2029 x 1427 pixels,  where each pixel represents an area of 0.09 ha or 900m².

![](Size_by_pixel.png)


 The chosen images from NASA were acquired on the website https://earthobservatory.nasa.gov/images/145888/making-sense-of-amazon-deforestation-patterns and it represents a fragment of the Caguán River located in Colombia.

![](LANDSAT2000.png)
![](LANDSAT2017.png)

**Description of steps to reach the objective**

 This type of quantification where pixels are related to measurements is known as photogrammetry. The project has 3 important phases: the first is pre-processing where the aim is to improve the image (eliminating noise through filters). The second phase is to define regions of interest and extract them (segmentation). Finally, the third phase consists of quantify a statistic comparing the established metrics.



 
 
 Final project for **[SCC0251 - Image Processing](https://uspdigital.usp.br/jupiterweb/jupDisciplina?sgldis=SCC0251)** @ ICMC/USP.
 
 
