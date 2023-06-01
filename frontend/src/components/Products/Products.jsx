import {
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Box,
  Checkbox,
  Container,
  FormControlLabel,
  FormGroup,
  Grid,
  Typography,
} from "@mui/material";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import { useEffect, useState } from "react";

const Products = () => {
  const baseUrl = `https://qsl-solutions.onrender.com/`;
  const [products, setProduct] = useState([]);
  const [filterData, setFilterData]=useState([])


  const [categoryList, setCategoryList] = useState([]);
  const [productType, setProductType] = useState([]);
  const [brandList, setBrandList] = useState([]);
  const [warrentyList, setWarrentyList] = useState([]);
  const [sellerList, setSellerList] = useState([]);

  const [productCatgory, setProductCategory] = useState("");
  const [productTypeFilter, setProductTypeFilter] = useState("");
  const [productBrand, setProductBrand] = useState("");
  console.log(productBrand);
  const [productWarrentey, setProductWarrenty] = useState("");
  const [productSeller, setProductSeller] = useState("");
  const [minPrice, setMinPrice]=useState("")
  const [maxPrice, setMaxPrice]=useState("")
  // const [filter, setfilter]=useState("")

  // product list data fetch
  useEffect(() => {
    const options = { method: "GET" };
    fetch("https://qsl-solutions.onrender.com/api/product/filter/list/", options)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setCategoryList(data?.catagory_list);
        setProductType(data?.product_type_list);
        setBrandList(data?.brand_list);
        setWarrentyList(data?.warrenty_list);
        setSellerList(data?.seller_list);
      })
      .catch((err) => console.error(err));
  }, []);

  // product data fetch
  useEffect(() => {
    const options = { method: "GET" };
    fetch("https://qsl-solutions.onrender.com/api/product/list/", options)
      .then((response) => response.json())
      .then((data) => {
        setProduct(data?.results);
        setFilterData(data?.results)
      })
      .catch((err) => console.error(err));
  }, []);

 
  // const url = `https://qsl-solutions.onrender.com/api/product/list/?catagory=${productCatgory}&sell_price_min=${minPrice}&brand=${productBrand}&sell_price_max=${maxPrice}&product_type=${productTypeFilter}&warrenty=${productWarrentey}&seller=${productSeller}`;

  useEffect(() => {
    const options = { method: "GET" };
    const url = `https://qsl-solutions.onrender.com/api/product/list/?&brand=${productBrand}`;
    console.log(url);
    fetch(url, options)
      .then((response) => response.json())
      .then((data) => {
        setFilterData(data?.results); 
      })
      .catch((err) => console.error(err));
  },[productBrand]);

  return (
    <Box>
      <Container>
        <Box>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={4} md={2.5}>
              <Box
                className="filter-side-0"
                boxShado="0px 0px 15px rgba(42, 110, 152, 0.23)"
                bgcolor="#fff"
                p={1}
                borderRadius="5px"
              >  <Accordion
              defaultExpanded={false}
              style={{ margin: "0", boxShadow: "none" }}
            >
              <AccordionSummary
                style={{ margin: "0", padding: "0px" }}
                expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                id="panel2a-header"
              >
                <Typography
                  sx={{
                    color: "#BC6277",
                    fontWeight: 500,
                    fontSize: 13,
                  }}
                >
                  Brand List
                </Typography>
              </AccordionSummary>
              <AccordionDetails style={{ margin: "0", padding: "0" }}>
                <Box>
                  <FormGroup>
                    {brandList?.map((brandList, index) => (
                      <FormControlLabel
                        key={index}
                        // value={"couple"}
                        value={brandList?.name}
                        onChange={(e) => setProductBrand(e.target.value)}
                        control={<Checkbox className="box-0" />}
                        label={
                          <Typography
                            sx={{
                              color: "#BC6277",
                              fontWeight: 500,
                              fontSize: 13,
                            }}
                          >
                            {brandList?.name}
                          </Typography>
                        }
                      />
                    ))}
                  </FormGroup>
                </Box>
              </AccordionDetails>
            </Accordion>
                <Accordion
                  defaultExpanded={true}
                  style={{ margin: "0", boxShadow: "none" }}
                >
                  <AccordionSummary
                    style={{ margin: "0", padding: "0px" }}
                    expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                    id="panel2a-header"
                  >
                    <Typography
                      sx={{
                        color: "#BC6277",
                        fontWeight: 500,
                        fontSize: 13,
                      }}
                    >
                      Catagory list
                    </Typography>
                  </AccordionSummary>
                  <AccordionDetails style={{ margin: "0", padding: "0" }}>
                    <Box>
                      <FormGroup>
                        {categoryList?.map((categoryList, index) => (
                          <FormControlLabel
                            key={index}
                            // value={"couple"}
                            control={<Checkbox className="box-0" />}
                            value={categoryList?.name}
                            onChange={(e) => setProductCategory(e.target.value)}
                            label={
                              <Typography
                                sx={{
                                  color: "#BC6277",
                                  fontWeight: 500,
                                  fontSize: 13,
                                }}
                              >
                                {categoryList?.name}
                              </Typography>
                            }
                          />
                        ))}
                      </FormGroup>
                    </Box>
                  </AccordionDetails>
                </Accordion>
                <Accordion
                  defaultExpanded={false}
                  style={{ margin: "0", boxShadow: "none" }}
                >
                  <AccordionSummary
                    style={{ margin: "0", padding: "0px" }}
                    expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                    id="panel2a-header"
                  >
                    <Typography
                      sx={{
                        color: "#BC6277",
                        fontWeight: 500,
                        fontSize: 13,
                      }}
                    >
                      Product Type
                    </Typography>
                  </AccordionSummary>
                  <AccordionDetails style={{ margin: "0", padding: "0" }}>
                    <Box>
                      <FormGroup>
                        {productType?.map((productType, index) => (
                          <FormControlLabel
                            key={index}
                            // value={"couple"}
                            control={<Checkbox className="box-0" />}
                            value={productType?.name}
                            onChange={(e) =>
                              setProductTypeFilter(e.target.value)
                            }
                            label={
                              <Typography
                                sx={{
                                  color: "#BC6277",
                                  fontWeight: 500,
                                  fontSize: 13,
                                }}
                              >
                                {productType?.name}
                              </Typography>
                            }
                          />
                        ))}
                      </FormGroup>
                    </Box>
                  </AccordionDetails>
                </Accordion>
              
                <Accordion
                  defaultExpanded={false}
                  style={{ margin: "0", boxShadow: "none" }}
                >
                  <AccordionSummary
                    style={{ margin: "0", padding: "0px" }}
                    expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                    id="panel2a-header"
                  >
                    <Typography
                      sx={{
                        color: "#BC6277",
                        fontWeight: 500,
                        fontSize: 13,
                      }}
                    >
                      Warrenty List
                    </Typography>
                  </AccordionSummary>
                  <AccordionDetails style={{ margin: "0", padding: "0" }}>
                    <Box>
                      <FormGroup>
                        {warrentyList?.map((warrentyList, index) => (
                          <FormControlLabel
                            key={index}
                            // value={"couple"}
                            value={warrentyList?.name}
                            onChange={(e) => setProductWarrenty(e.target.value)}
                            control={<Checkbox className="box-0" />}
                            label={
                              <Typography
                                sx={{
                                  color: "#BC6277",
                                  fontWeight: 500,
                                  fontSize: 13,
                                }}
                              >
                                {warrentyList?.name}
                              </Typography>
                            }
                          />
                        ))}
                      </FormGroup>
                    </Box>
                  </AccordionDetails>
                </Accordion>
                <Accordion
                  defaultExpanded={false}
                  style={{ margin: "0", boxShadow: "none" }}
                >
                  <AccordionSummary
                    style={{ margin: "0", padding: "0px" }}
                    expandIcon={<KeyboardArrowUpIcon color="#BC6277" />}
                    id="panel2a-header"
                  >
                    <Typography
                      sx={{
                        color: "#BC6277",
                        fontWeight: 500,
                        fontSize: 13,
                      }}
                    >
                      Seller List
                    </Typography>
                  </AccordionSummary>
                  <AccordionDetails style={{ margin: "0", padding: "0" }}>
                    <Box>
                      <FormGroup>
                        {sellerList?.map((sellerList, index) => (
                          <FormControlLabel
                            key={index}
                            // value={"couple"}
                            value={sellerList?.name}
                            onChange={(e) => setProductSeller(e.target.value)}
                            control={<Checkbox className="box-0" />}
                            label={
                              <Typography
                                sx={{
                                  color: "#BC6277",
                                  fontWeight: 500,
                                  fontSize: 13,
                                }}
                              >
                                {sellerList?.name}
                              </Typography>
                            }
                          />
                        ))}
                      </FormGroup>
                    </Box>
                  </AccordionDetails>
                </Accordion>
              </Box>
            </Grid>

            <Grid item xs={12} sm={8} md={9.5}>
              <Grid container>
                {filterData?.map((product, index) => (
                  <Grid key={index} item xs={12} sm={6} md={4}>
                    <Box
                      sx={{ backgroundColor: "#ccc", padding: "15px", m: 0.5 }}
                    >
                      <Box>
                        <img
                          src={`${baseUrl}${product?.image}`}
                          alt="productImg"
                          style={{ width: "100%", height: "200px" }}
                        />
                      </Box>
                      <Box style={{ textAlign: "center" }} my={1}>
                        <Typography>Name:{product?.name}</Typography>
                      </Box>
                      <Typography>{product?.brand}</Typography>
                      <Box style={{ textAlign: "center" }} mb={2}>
                        <Typography>
                          Price:{product?.discounted_sell_price}
                        </Typography>
                        <del>Price:{product?.normal_sell_price}</del>
                      </Box>

                      <Box
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                        }}
                      >
                        <button
                          style={{
                            width: "80px",
                            height: "30px",
                            cursor: "pointer",
                            background: "#702C8B",
                            border: "none",
                            color: "#fff",
                            borderRadius: "5px",
                          }}
                        >
                          Book{" "}
                        </button>
                        <button
                          style={{
                            width: "80px",
                            height: "30px",
                            cursor: "pointer",
                            background: "#BC6277",
                            border: "none",
                            color: "#fff",
                            borderRadius: "5px",
                          }}
                        >
                          wishList
                        </button>
                      </Box>
                    </Box>
                  </Grid>
                ))}
              </Grid>
            </Grid>
          </Grid>
        </Box>
      </Container>
    </Box>
  );
};

export default Products;
