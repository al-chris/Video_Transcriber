function showSpinner() {
    document.getElementById("spinner").style.display = "inline-block";
}

function uploadFile() {
    const fileInput = document.getElementById("fileToUpload");
    const maxFileSize = 20 * 1024 * 1024; // 16MB in bytes

    if (fileInput.files.length === 0) {
        alert("Please select a file.");
        return;
    }

    const selectedFile = fileInput.files[0];

    if (selectedFile.size > maxFileSize) {
        alert("File size exceeds the 20MB limit.");
        return;
    }

    showSpinner();

    const formData = new FormData();
    formData.append("fileToUpload", selectedFile);

    fetch("/process", {
        method: "POST",
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Get the response as text
        } else {
            alert("Error uploading file.");
            return null;
        }
    })
    .then(data => {
        if (data !== null) {
            document.getElementById("summary").textContent = data[0];
            document.getElementById("textToCopy").value = data[1];
        }
        document.getElementById("spinner").style.display = "none";
        document.getElementById("fileToUpload").value = ""; // Clear file input
        document.getElementById("downloadFileBtn").style.display = "inline-block";
    })
    .catch(error => {
        console.error("Error:", error);
        alert("An error occurred while uploading the file.");
        document.getElementById("spinner").style.display = "none";
    });
}

function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle("dark-mode");
}

function copyToClipboard() {
    // const textToCopy = "Text you want to copy"; // Replace with your desired text
    const textToCopy = document.getElementById("textToCopy").value;
    const textArea = document.createElement("textarea");
    textArea.value = textToCopy;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
    alert("Text copied to clipboard: " + textToCopy);
}

function downloadTextFile() {
    const textToDownload = document.getElementById("textToCopy").value;
    const fileName = "downloaded_file.txt";
    const blob = new Blob([textToDownload], { type: "text/plain" });

    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function updateFileName() {
    const fileInput = document.getElementById("fileToUpload");
    const selectedFileName = document.getElementById("selectedFileName");
    selectedFileName.textContent = fileInput.files[0].name;
}