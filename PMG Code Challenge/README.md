# CSV Combiner

A command line program that takes several CSV files as arguments and combines them. Additionally, the combined csv
will contain another column titled `filename` which indicates that row's file of origin. In my solution, some issues were encountered
with the desired cmd formatting, the resolution and details of the problem are listed in the section titled "NOTE:".

## Input & Output
We will run your code as follows
```
$ ./csv-combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

However, the CSV files inside the fixtures are not the only files we will run
through. We will run your code through files > 2 GB to see if you hit memory limits.

#### NOTE: #### 
On a windows environment, the ">" character represents redirecting output, resulting in the combined.csv file to contain the arguments.
As such, my submission will be accompanied by a video demonstration for sake of proving the script's functionality as I have no other system to
test with. 
```
$ py csv-combiner.php fixtures/accessories.csv fixtures/clothing.csv > combined.csv
```
Demonstration: https://youtu.be/e5evxTLLTa0 

## Example

Given two input files named `clothing.csv` and `accessories.csv`.

|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

Your script would output

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|
