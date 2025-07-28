class Trie {
    public root: TrieNode

    constructor() {
        this.root = new TrieNode(NaN);
    }

    addList(nums: number[]) {
        this.root.addChildren(nums);
    }

    to2DArray(): number[][] {
        const master: number[][] = []
        for (let node of this.root.children) {
            const [value, trieNode] = node
            let list = []
            if (trieNode.hasChildren())
                trieNode.dig(master, list)
        }
        return master.sort((a: number[], b: number[]) => {
            if (a[0] === b[0]) {
                if (a[1] === b[1]) {
                    return a[2] - b[2]
                }
                return a[1] - b[1]
            }
            return a[0] - b[0]
        })
    }
}

class TrieNode {
    public children: Map<number, TrieNode> = new Map()
    public value: number

    constructor(value: number) {
        this.value = value;
    }

    addChildren(nums: number[]) {
        if (this.children.get(nums[0])) {
            if (nums.length == 1) {
                return;
            } else {
                this.children.get(nums[0])?.addChildren(nums.slice(1))
            }
        } else {
            this.children.set(nums[0], new TrieNode(nums[0]))
            if (nums.length == 1) {
                return;
            }
            else {
                this.children.get(nums[0])?.addChildren(nums.slice(1))
            }
        }
    }
    hasChildren() {
        return this.children.size > 0
    }

    dig(master: number[][], list: number[]) {
        const listCopy = [...list]
        if (!this.hasChildren()) {
            listCopy.push(this.value);
            master.push(listCopy.sort())
            return;
        }
        listCopy.push(this.value);
        for (let tuple of this.children) {
            const [value, child] = tuple
            child.dig(master, listCopy);
        }
    }
}

function threeSum(nums: number[]): number[][] {
    const resultSet = new Trie()
    nums = nums.sort()
    for (let i = 0; i < nums.length - 2; i++) {
        if (nums[i] > 0) break
        let left = i + 1;
        let right = nums.length - 1
        while (left < right) {
            const sum = nums[left] + nums[right] + nums[i]
            if (sum === 0) {
                resultSet.addList([nums[i], nums[left], nums[right]])
                // while (left < right && nums[left] === nums[left + 1]) left++
                // Skip duplicates for right pointer
                // while (left < right && nums[right] === nums[right - 1]) right--
                left++
                right--
            } else if (sum < 0) {
                left++
            } else {
                right--;
            }
        }
    }
    return resultSet.to2DArray()
};

console.log(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))