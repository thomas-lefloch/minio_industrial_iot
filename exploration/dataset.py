import pandas

dataset_root_path = "source_dataset"
dataset_files = [
    f"{dataset_root_path}/LineA_Stable_10K.csv",
    f"{dataset_root_path}/LineB_Flux.csv",
    f"{dataset_root_path}/LineC_Turbulent.csv",
    f"{dataset_root_path}/LineD_SpikeControl.csv",
    f"{dataset_root_path}/LineE_SmoothRun.csv"
]

for file in dataset_files:
    csv = pandas.read_csv(file)
    print ( "-----", file, "-----")
    print("# lignes:", len(csv))
    print(csv.dtypes)
    
    # markdown copy-paste
    # with open(file, "r") as f:
    #     entete = f.readline().strip()
    # filename = file.split("/")[-1]
    
    # print("|", "|".join([filename, str(len(csv)), entete]), "|")

