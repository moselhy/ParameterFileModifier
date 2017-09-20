# Modifies Registration Parameter Files

### If you have many files like this:

(Transform "WeightedCombinationTransform")<br />
(NumberOfParameters 2)<br />
(TransformParameters 0.5 0.5)<br />
(SubTransforms "YYYZ_WeightedTransforms/par0029-step1-identityCPR.txt" "BBA_04_ODDtoEVEN_lin_false/TransformParameters.1.txt")<br />
(AutomaticScalesEstimation "true")<br />
(FixedImageDimension 3)<br />
(MovingImageDimension 3)<br />
(FixedInternalImagePixelType "float")<br />
(MovingInternalImagePixelType "float")<br />
(Index 0 0 0)<br />
(Size 256 256 60)<br />
(Spacing 1.9530999660 1.9530999660 5.0000000000)<br />
(Origin -1.9530999660 -1.9530999660 5.0000000000)<br />
(Direction -1.0000000000 0.0000000000 0.0000000000 0.0000000000 -1.0000000000 0.0000000000 0.0000000000 0.0000000000 1.0000000000)<br />
(UseDirectionCosines "true")<br />
(ResampleInterpolator "FinalBSplineInterpolator")<br />
(FinalBSplineInterpolationOrder 3)<br />
(Resampler "DefaultResampler")<br />
(DefaultPixelValue -1.000000)<br />
(ResultImageFormat "nii")<br />
(ResultImagePixelType "float")<br />
(CompressResultImage "false")<br />

### And you want to change the value of a certain tag (e.g. `Size`) to a certain value (e.g. `256 256 64`)

### You would run this:

`python modTag.py DIRECTORY Size 256 256 64`

###### Where `DIRECTORY` is the relative path to the directory containing all the parameter files

## A few things worth mentioning:

1) The directory should not have any binary files, try to only keep the parameter files there, or it may take a long time to go through it, depending on your RAM size

2) You can escape the quotation marks ("") by using the escape character followed by a quotation (\\")

For example, To change FixedInternalImagePixelType from "float" to "int", you would type:

`python modTag.py DIRECTORY FixedInternalImagePixelType \"int\"`