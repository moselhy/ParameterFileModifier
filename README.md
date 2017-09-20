# Modifies Registration Parameter Files

If you have many files like this:

(Transform "WeightedCombinationTransform")
(NumberOfParameters 2)
(TransformParameters 0.5 0.5)
(SubTransforms "YYYZ_WeightedTransforms/par0029-step1-identityCPR.txt" "BBA_04_ODDtoEVEN_lin_false/TransformParameters.1.txt")
(AutomaticScalesEstimation "true")
(FixedImageDimension 3)
(MovingImageDimension 3)
(FixedInternalImagePixelType "float")
(MovingInternalImagePixelType "float")
(Index 0 0 0)
(Size 256 256 60)
(Spacing 1.9530999660 1.9530999660 5.0000000000)
(Origin -1.9530999660 -1.9530999660 5.0000000000)
(Direction -1.0000000000 0.0000000000 0.0000000000 0.0000000000 -1.0000000000 0.0000000000 0.0000000000 0.0000000000 1.0000000000)
(UseDirectionCosines "true")
(ResampleInterpolator "FinalBSplineInterpolator")
(FinalBSplineInterpolationOrder 3)
(Resampler "DefaultResampler")
(DefaultPixelValue -1.000000)
(ResultImageFormat "nii")
(ResultImagePixelType "float")
(CompressResultImage "false")

And you want to change the value of a certain tag (e.g. Size) to a certain value (e.g. 256 256 64)

You would run this:

`python modTag.py DIRECTORY Size 256 256 64`

Where `DIRECTORY` is the relative path to the directory containing all the parameter files

## A few things worth mentioning:
<br />

1) The directory should not have any binary files, try to only keep the parameter files there, or it may take a long time to go through it, depending on your RAM size
2) You can escape the quotation marks ("") by using the escape character followed by a quotation (\\")
For example, To change FixedInternalImagePixelType from "float" to "int", you would type:
`python modTag.py DIRECTORY FixedInternalImagePixelType \"int\"`