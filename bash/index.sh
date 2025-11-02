# this folder is to practice with bash scripts

echo "${array[0]}"

echo "${array[@]}"

echo "${#array[@}"

for item in "${array[@]}"; do
	echo "$item"
done